import os
import json
import requests
from bs4 import BeautifulSoup
import concurrent.futures

BASE_URL = 'https://vstup.osvita.ua/r27/'
FILENAME = 'universities.json'

#Парсит 1 сайт
def fetch_url(url: str) -> requests.models.Response:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        return response
    except requests.RequestException as e:
        print(f"Request failed for {url}: {e}")
        return None

#Получить название сайта с парсинга
def getUniversityTitle(response: requests.models.Response) -> str:
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('h1').get_text(strip=True) if soup.find('h1') else 'Unknown University'

#Многопоточный парсинг
def scrapeUniversities() -> dict:
    universities = {}
    page_number = 1
    consecutive_errors = 0

    while True:
        urls = [f"{BASE_URL}{i}/" for i in range(page_number, page_number + 10)]
        page_number += 10
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            responses = executor.map(fetch_url, urls)

        batch_universities = {}
        for response in responses:
            if response and response.status_code == 200:
                title = getUniversityTitle(response)
                batch_universities[title] = response.url
                print(f"University with url: {response.url} | Done")
            else:
                consecutive_errors += 1
                if consecutive_errors == 10:
                    print("Too many consecutive errors, stopping the scraping.")
                    return universities

        if batch_universities:
            universities.update(batch_universities)
            consecutive_errors = 0

    return universities

#Получение всех университетов
def loadUniversities() -> dict:
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', encoding='utf-8') as file:
            return json.load(file)
    else:
        universities = scrapeUniversities()
        with open(FILENAME, 'w', encoding='utf-8') as file:
            json.dump(universities, file, ensure_ascii=False, indent=4)
        return universities

#Получение топ университетов
def loadTopUniversity() -> list:
    url = 'https://osvita.ua/vnz/rating/92375/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('a', target="_blank")
    univers = list()
    for i in links:
        univers.append(i.text.strip())
    return univers

if __name__ == "__main__":
    universities_data = loadUniversities()
    print(f"Loaded {len(universities_data)} universities.")

