import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        headers = soup.find_all('h1')  # Можно изменить на другие теги заголовков, например, 'h2', 'h3', и т.д.

        for header in headers:
            print(header.text)
    else:
        print("Failed to fetch the webpage")

if __name__ == "__main__":
    url = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'  # Замените на URL нужного сайта
    simple_web_scraper(url)
