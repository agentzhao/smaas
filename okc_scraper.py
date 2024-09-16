from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
from getpass import getpass
import time
PATH = "C:\Program Files (x86)\geckodriver.exe"
options = Options()
options.headless = False
driver = webdriver.Firefox(options=options, executable_path=PATH)
driver.set_window_size(1024, 768)

questions = "https://www.okcupid.com/profile/18025740128926849451/questions?rqid="
website = "https://www.okcupid.com"
driver.get(website)
time.sleep(2)

driver.find_element_by_css_selector(".splashdtf-header-signin-splashButton").click()

email_textbox = driver.find_element_by_id("username")
email = "agentzhao26@gmail.com"
email_textbox.send_keys(email)

password_textbox = driver.find_element_by_id("password")
password = "Rubixcub3"
password_textbox.send_keys(password)

driver.find_element_by_css_selector(".login-actions-button").click()
time.sleep(1)

import json
file1 = open("okc_questionbank.txt", "a")

id = 8845
while True:
    try:
        driver.get(questions + str(id))
        time.sleep(2)
        question = driver.find_elements_by_css_selector(".questionspage-multipartquestion")
        data = question[0].text.split('Answers you’ll accept')[0].split('\n')
        array = [id, data[0], data[2:-1]]
        file1.write(str(array) + '\n')
        id += 1
    except IndexError:
        id -= 1
        continue

file1.close()




