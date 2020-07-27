from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import sys
import time
import re
import csv


def write(data):
    with open('marks_gvx.csv', mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(data)



options = Options()

#  Code to disable notifications pop up of Chrome Browser
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
# options.add_argument("user-data-dir=/home/tuhalang/Documents/profile/1")
# options.add_argument("headless")

try:
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(), options=options
    )
    driver.get('http://222.255.113.131/')
    for i in range(120001, 121000):
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtName"]').clear()
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_txtName"]').send_keys(str(i))
        driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_btnSearch"]').click()
        try:
            tr = driver.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_grdKetqua"]/tbody/tr[2]')
            tds = tr.find_elements_by_tag_name('td')
            data = []
            for td in tds:
                data.append(td.text)
                print(td.text)
            if len(data) > 0:
                write(data[:4])
        except:
            pass
        

except Exception as e:
    print(e)