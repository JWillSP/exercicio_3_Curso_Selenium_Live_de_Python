import re
import time
from selenium import webdriver

def clicar_em(text, ele):
    ele.find_element_by_link_text(text).click()
    time.sleep(2)

init_url = r"C:\Users\Public\Downloads\geckodriver.exe"

nav = webdriver.Firefox(executable_path=init_url)

#exercicio_03.html
nav.get('https://selenium.dunossauro.live/exercicio_03.html')

time.sleep(2)

clicar_em('Começar por aqui', nav)

#page_1.html
main1 = nav.find_element_by_tag_name('main')

list_Ps = [ele
           for ele in main1.find_elements_by_tag_name('p')
           if '=' in ele.text]

expression = list_Ps[0].text

resultado1 = eval(expression.split('=')[0])

items_list = main1.find_elements_by_tag_name('li')

another = [ele for ele in items_list if ele.text != str(resultado1)][0]

clicar_em(another.text, another)

time.sleep(6)

#page_2.html2
nav.refresh()

time.sleep(10)

clicar_em(nav.title, nav)

#page_3.html
url = nav.current_url

path = re.search(r'//.+/(.+)', url).group(1)

clicar_em(path,nav)

#page_4.html
nav.refresh()
