import re
import time
from selenium import webdriver

init_url = r"C:\Users\Public\Downloads\geckodriver.exe"

nav = webdriver.Firefox(executable_path=init_url)

#exercicio_03.html
nav.get('https://selenium.dunossauro.live/exercicio_03.html')

time.sleep(2)

main = nav.find_element_by_tag_name('main')

start_here = main.find_element_by_link_text('Começar por aqui')

start_here.click()

time.sleep(2)

#page_1.html
main1 = nav.find_element_by_tag_name('main')

list_Ps = [ele
           for ele in main1.find_elements_by_tag_name('p')
           if '=' in ele.text]

expression = list_Ps[0].text

resultado1 = eval(expression.split('=')[0])

items_list = main1.find_elements_by_tag_name('li')

another = [ele for ele in items_list if ele.text != str(resultado1)][0]

to_click = another.find_element_by_link_text(another.text)

to_click.click()

time.sleep(10)

#page_2.html2
nav.refresh()

time.sleep(10)

nav.title

to_click2 = nav.find_element_by_link_text(nav.title)

to_click2.click()

time.sleep(2)

#page_3.html
url = nav.current_url

path = re.search(r'//.+/(.+)', url).group(1)

to_click3 = nav.find_element_by_link_text(path)

to_click3.click()

time.sleep(2)

#page_4.html
nav.refresh()
