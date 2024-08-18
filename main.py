import requests
from bs4 import BeautifulSoup
import University

allUniversities = University.loadUniversities()
topUniversities = University.loadTopUniversity()
print(topUniversities)