from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver = webdriver.Chrome(executable_path=r'D:/chromedriver_win32/chromedriver.exe')

url = 'https://rvrjcce.ac.in/examcell/results/regnoresultsR.php?'

driver.get(url)

inp = '/html/body/div[1]/form/table/tbody/tr/td[3]/input'

rollno = ['y17cs0' + str(i) for i in range(61, 100)]
print(rollno)

for num in rollno:
    
    driver.find_element(By.XPATH, inp).send_keys(num)

    time.sleep(5)

    #driver.find_element(By.XPATH, inp).clear()

    marks_rows = '/html/body/div[1]/form/div/div/div/table/tbody/tr'

    rows = len(driver.find_elements_by_xpath(marks_rows))

    marks_cols = '/html/body/div[1]/form/div/div/div/table/tbody/tr[3]/td'
    
    cols = len(driver.find_elements_by_xpath(marks_cols))

    print(rows - 1, "rows including header section", cols, "columns")

    for i in range(2, 7):
        for j in range(1, 13):
            if(i == 2):
                col_xpath = marks_rows + '[' + str(i) + ']' + '/th[' + str(j) + ']'
            else:
                col_xpath = marks_rows + '[' + str(i) + ']' + '/td[' + str(j) + ']'

            value = driver.find_element_by_xpath(col_xpath).text
            
            print('{:20}'.format(value), end = '')
            
        print()

    driver.find_element(By.XPATH, inp).clear()
    
    time.sleep(1)
    
driver.quit()

