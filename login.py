from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://smemi.personifycloud.com/SSO/Login.aspx?vi=9&vt=66d4ecf86b5608888d8652e1223449493e998db93fc3ed5836ab7ab4ca0548afabee4629bbd2edbeb1b3bc3f4bc1e680bf5908fb815f9eb6aae99af0f6050d346aa8ded3a7d1bf37956b2758f3be5602a3f400685843ec1a19b579f31adc37ac")

username = driver.find_element_by_id("main_LoginTextBox")
username.clear()
username.send_keys("satish.penmetsa@rapidbizapps.com")

password = driver.find_element_by_id("main_PasswordTextBox")
password.clear()
password.send_keys("empyr3An")

driver.find_element_by_id("main_SubmitButton").click()

driver.find_element_by_id("MainCopy_ctl02_Tab2").click()

select = Select(driver.find_element_by_id('MainCopy_ctl08_FindStateProvinceCode'))

select.select_by_visible_text('Alabama')

#Search page java script button
find_btn = driver.find_element_by_xpath('//*[@id="MainCopy_ctl26_FindContacts"]')
driver.execute_script("arguments[0].click();", find_btn)

#Finding elements by class name
member_names = driver.find_elements_by_class_name("member-name")
names = [x.text for x in member_names]

print("names:")
for name in names:
    print(name)