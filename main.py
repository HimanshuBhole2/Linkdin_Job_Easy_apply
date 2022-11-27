from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver .common .keys import Keys
from time import sleep



CHROME_DRIVER_PATH = "YOUR DRIVER PATH"
driver = webdriver.Chrome(executable_path = CHROME_DRIVER_PATH)


driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%" \
"2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")
sleep(3)
continue_link = driver.find_element(By.LINK_TEXT, 'Sign in')
print(continue_link)
continue_link.send_keys(Keys.ENTER)
Username = driver.find_element(By.NAME,"session_key" )
print(Username)
sleep(2)
Username.send_keys("Your EMail")
passward = driver.find_element(By.NAME, "session_password")
sleep(1)
passward.send_keys("Your Passward")
sleep(2)

signin = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/form/div[3]/button")
print(signin)
signin.send_keys(Keys.ENTER)
sleep(6)
easy_apply_btn = driver.find_elements(By.CLASS_NAME, 'jobs-apply-button')
for easy_apply in easy_apply_btn:
    easy_apply.click()
    sleep(2)
    phone_no = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/div/div/div[3]/div[2]/div/div/input')
    print(phone_no)
    phone_no.send_keys("9545343323")
    sleep(1)
    next = driver.find_element(By.ID, "ember353")
    print(next)
    next.send_keys(Keys.ENTER)
    sleep(1)
    click_review = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end .artdeco-button--primary').click()
    sleep(3)
    click_submit = driver.find_element(By.CSS_SELECTOR, '.justify-flex-end .artdeco-button--primary').click()
    sleep(2)