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

select.select_by_visible_text('Arizona')

#Search page java script button
find_btn = driver.find_element_by_xpath('//*[@id="MainCopy_ctl26_FindContacts"]')
driver.execute_script("arguments[0].click();", find_btn)

select_page = Select(driver.find_element_by_id('MainCopy_ctl26_ResultsPerPage'))
select_page.select_by_visible_text('100 per page')

def extractor():
    # Finding elements by class name
    member_names = driver.find_elements_by_class_name("member-name")
    names = [x.text for x in member_names]

    for name in names:
        print(name)

    member_role = driver.find_elements_by_class_name("company-title")
    roles = [x.text for x in member_role]

    for role in roles:
        print(role)

    member_company = driver.find_elements_by_class_name("company-name")
    companies = [x.text for x in member_company]

    for company in companies:
        print(company)

    member_mail = driver.find_elements_by_class_name("member-email")
    mails = [x.text for x in member_mail]

    for mail in mails:
        print(mail)

    member_address = driver.find_elements_by_class_name("list-address-panel")
    addresses = [x.text for x in member_address]

    for address in addresses:
        main_address = address.split(',', 1)[0]
        print(main_address)

# extractor()
#
# next_btn = driver.find_element_by_xpath('//*[@id="MainCopy_ctl26_Pager_NextPageButton"]')
# driver.execute_script("arguments[0].click();", next_btn)
#
# extractor()


#Function for extracting individual profile data
def profile_data(xpath) :
    #Finding profile element by Xpath
    profile = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].click();", profile)

    #Extracting individual elements on profile page
    member_name = driver.find_element_by_id('MainCopy_ctl23_lblName')
    member_jobtitle = driver.find_element_by_id('MainCopy_ctl27_DisplayPresentJob1_JobDepartmentPanel')
    member_company = driver.find_element_by_id('MainCopy_ctl27_DisplayPresentJob1_CompanyNamePanel')
    member_mail = driver.find_element_by_id('MainCopy_ctl14_presentJob_EmailAddress')
    member_phone = driver.find_element_by_id('MainCopy_ctl14_presentJob_Phone1Panel')
    member_city = driver.find_element_by_id('MainCopy_ctl14_presentJob_CityStateRegionPanel')

    print(member_name.text + "," + member_jobtitle.text + "," + member_company.text + "," + member_mail.text + "," + member_city.text + "," + member_phone.text)


for i in range(2, 4):
    #Creating xpaths for individual profile
    profile_xpath = '//*[@id="MainCopy_ctl26_Contacts_DisplayName_' + str(i) + '"]'

    #Calling profile_data() function with xpath parameter
    profile_data(profile_xpath)

    #clicking back button before another iteration
    driver.execute_script("window.history.go(-1)")





