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
p = nav.find_element_by_xpath('//p[contains(text(),"=")]')

rtn = eval(p.text.split('=')[0])

outra = nav.find_element_by_xpath(f'//main//li[not(contains(text(),"{rtn}"))]')

clicar_em(outra.text, outra)

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
