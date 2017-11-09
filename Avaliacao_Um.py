from bs4 import BeautifulSoup
import requests

def search(keyword, url, deth):
    
    response = requests.get(url)
    html_com_tags = response.text
    html_sem_tags = BeautifulSoup(html_com_tags, 'html.parser')
    contexto = ""

    for i in range(len(html_sem_tags.text)):
        if (html_sem_tags.text[i:i + len(keyword)] == keyword):
            contexto = html_sem_tags.text[i - 10:i + len(keyword) + 11]
            while deth > 0:
                search(keyword, url, deth - 1)

    print(contexto + " " + url)

search('animais vertebrados', 'https://www.google.com/search?q=peixe', 0)

