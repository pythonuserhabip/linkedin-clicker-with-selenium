import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3231607692&f_LF=f_AL&geoId=102257491&keywords=python%"
           "20developer&location=London%2C%20England%2C%20United%20Kingdom")

sign_in_button = driver.find_element("css selector", ".nav__button-secondary")
sign_in_button.click()

time.sleep(2)

user_name_field = driver.find_element("css selector", "#username")
user_name_field.send_keys("EMAIL")

password_field = driver.find_element("css selector", "#password")
password_field.send_keys("PASSWORD")

sign_in = driver.find_element("css selector", ".btn__primary--large")
sign_in.click()

# apply_button = driver.find_element("css selector", ".jobs-apply-button")
# apply_button.click()
#
# phone_num = driver.find_element("css selector", ".ember-text-field")
# phone_num.send_keys("1234567890")

all_listings = driver.find_elements("class name", "jobs-search-results__list-item")
for job in all_listings:
    actions = ActionChains(driver)
    actions.move_to_element(job).perform()
    job.click()
    time.sleep(2)
    save_job_button = driver.find_element("class name", "jobs-save-button")
    save_job_button.click()
    time.sleep(2)
    dialog_box_button = driver.find_element("class name", "artdeco-toast-item__dismiss")
    dialog_box_button.click()
    time.sleep(1)

# driver.quit()