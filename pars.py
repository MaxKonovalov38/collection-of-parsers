# Импортируем модули
import requests
from bs4 import BeautifulSoup as bs

# Эмулируем поведение браузера
headers = {'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0'}

# Адресс сайта
base_url = 'https://irkutsk.hh.ru/search/vacancy?area=35&clusters=true&enable_snippets=true&specialization=10.470&industry=47&from=cluster_industry'

# Файл в которвый будем сбрасывать данные
out = 'text.txt'

# Функция парсера
def hh_parse(base_url, headers):
    jobs = []
    # Эмулируем пользователя
    session = requests.Session()
    request = session.get(base_url, headers=headers)
    # Если сайт доступен по base_url, то выполнить условие
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        output_file = open(out, 'a')
        # Выводим отформатированный список данных
        for div in divs:
            # Выводим заголовок вакансии
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            # Выводим адрес вакансии
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            # Выводим название компании
            company = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-employer'}).text
            # Выводим описание компании
            text1 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            # Выводим описание вакансии
            text2 = div.find('div', attrs={'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            #
            content = 'Условия:\n' + text1 + '\nТребования к кандидату:\n' + text2
            #
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'content': content
                })
            output_file.write(content)
        print(jobs)
        output_file.close()
    else:
        print('Error!')

hh_parse(base_url, headers)

# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0
# https://irkutsk.hh.ru/search/vacancy?area=35&clusters=true&enable_snippets=true&specialization=10.470&industry=47&from=cluster_industry

# https://irkutsk.hh.ru/search/vacancy?area=35&clusters=true&enable_snippets=true&specialization=10.470