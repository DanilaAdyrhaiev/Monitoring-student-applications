import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from education import UniversityService, FacultyService, StudentService
from education import University, Faculty, Student

univerService = UniversityService()

def getUniversityTitle(response: requests.models.Response) -> str:
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('h2').get_text(strip=True)

def getFacultyTitle(response: requests.models.Response) -> str:
    soup = BeautifulSoup(response.text, 'html.parser')
    program_tag = soup.find('b', string="Факультет: ")
    return program_tag.next_sibling.strip().strip('"')

def getProgram(response: requests.models.Response) -> str:
    soup = BeautifulSoup(response.text, 'html.parser')
    program_tag = soup.find('b', string="Освітня програма: ")
    return program_tag.next_sibling.strip().strip('"')

def getStudents(response: requests.models.Response) -> list:
    driver = webdriver.Chrome()
    driver.get(response.url)
    while True:
        try:
            detail_link = WebDriverWait(driver, 1).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='detail-link']"))
            )
            driver.execute_script("arguments[0].click();", detail_link)
        except Exception:
            break
    page_source = driver.page_source
    driver.quit()
    
    soup = BeautifulSoup(page_source, 'html.parser')
    rows = soup.find_all('tr', class_=lambda x: x and x.startswith('rstatus'))
    
    students = []
    for row in rows:
        name = row.find('td', {'data-th': 'ПІБ'}).text.strip()
        rating_tag = row.find('td', {'data-th': 'Бал'})
        rating = rating_tag.text.strip() if rating_tag else 'N/A'
        students.append(Student(name, rating))
    
    return students

def createFaculty(response: requests.models.Response) -> Faculty:
    university_title = getUniversityTitle(response)
    university = univerService.find_university(university_title)
    #используем количество факультетов
    if university:
        number_of_faculties = len(university.faculties)
    else:
        number_of_faculties = 0
    
    faculty_title = getFacultyTitle(response)
    program = getProgram(response)
    students = getStudents(response)

    faculty_name = f"{faculty_title} - {number_of_faculties + 1}"
    return Faculty(faculty_name, program, students)


def writeUniversity(url: str) -> None:
    response = requests.get(url)
    title = getUniversityTitle(response)
    university = univerService.find_university(title)
    faculty = createFaculty(response)
    
    if university is None:
        faculty_service = FacultyService({faculty.name: faculty})
        new_university = University(title, faculty_service.get_all())
        univerService.add_university(new_university)
    else:
        existing_faculties = university.faculties
        faculty_name = f"{faculty.name} - {len(existing_faculties) + 1}"
        faculty.name = faculty_name
        existing_faculties[faculty_name] = faculty
        university.faculties = existing_faculties
        univerService.edit_university(university)

def CheckMyUniversity(univers: list) -> UniversityService:
    for univer in univers:
        writeUniversity(univer)
    return univerService
