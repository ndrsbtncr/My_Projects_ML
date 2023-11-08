from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()


browser.get('https://www.indeed.com/career/human-resources-manager/salaries')


sleep(5)  

periodo = 'MONTHLY'

select = Select(browser.find_element(By.ID, 'pay-period-selector'))
select.select_by_value(periodo)

sleep(5)  

elements = browser.find_elements(By.CLASS_NAME, 'css-15so73c.e19afand0')
salaries = browser.find_elements(By.CLASS_NAME, 'css-k60owf.e1wnkr790')

with open('indeed_info.txt', 'w') as archivo:

    for i in range(len(salaries)):
        company_name = elements[i].text
        salary_info = salaries[i].text.split()
        salary = salary_info[0]
        #print(f"{company_name}: {salary} per {periodo.lower()}")
        
        archivo.write(company_name + " " + salary + " " + periodo.lower() + '\n')

sleep(5)  
browser.quit()