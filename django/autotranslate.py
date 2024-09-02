from selenium import webdriver
from bs4 import BeautifulSoup
import time
import json

def scrape(webmsg):
    driver = webdriver.Chrome()  
    ### change url by define lang translate from and to 
    driver.get('https://translate.google.com/?sl=fr&tl=ar&op=translate')

    input_field = driver.find_element('css selector', 'textarea[aria-label="Source text"]')
    input_field.send_keys(webmsg)
    time.sleep(3)  

    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    if soup.find('span', class_='ryNqvb'):
        translated_text = soup.find('span', class_='ryNqvb').text
    else:
        translated_text = ''
    
    driver.quit()
    return translated_text

def extract_empty_msgstr(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    translated_data = {}
    
    for key, value in data.items():
        print(f"Key: \"{key}\"")
        new_value = scrape(value)
        translated_data[key] = new_value
        print(f"Translated Value: \"{translated_data[key]}\"")
        print('-' * 40)
    
    with open('translated_file.json', 'w', encoding='utf-8') as file:
        json.dump(translated_data, file, ensure_ascii=False, indent=4)

### change with your current json file to be translated
extract_empty_msgstr('jsontest.json')
