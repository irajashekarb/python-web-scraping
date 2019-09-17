# Importing Dependencies
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

# Intiatlizing chrome web driver
driver = webdriver.Chrome()

# opening link
driver.get("https://smemi.personifycloud.com/SSO/Login.aspx?vi=9&vt=66d4ecf86b5608888d8652e1223449493e998db93fc3ed5836ab7ab4ca0548afabee4629bbd2edbeb1b3bc3f4bc1e680bf5908fb815f9eb6aae99af0f6050d346aa8ded3a7d1bf37956b2758f3be5602a3f400685843ec1a19b579f31adc37ac")

# username
username = driver.find_element_by_id("main_LoginTextBox")
username.clear()
username.send_keys("satish.penmetsa@rapidbizapps.com")

# password
password = driver.find_element_by_id("main_PasswordTextBox")
password.clear()
password.send_keys("empyr3An")

# Finding submit button
driver.find_element_by_id("main_SubmitButton").click()

driver.find_element_by_id("MainCopy_ctl02_Tab2").click()

# using Select GUI dependency for selecting one element from list of elements
select = Select(driver.find_element_by_id('MainCopy_ctl08_FindStateProvinceCode'))
select.select_by_visible_text('')

# Sending parameters to city dialog box
# city = driver.find_element_by_id('MainCopy_ctl08_FindCity')
# city.send_keys('')

# Search page java script button
find_btn = driver.find_element_by_xpath('//*[@id="MainCopy_ctl26_FindContacts"]')
driver.execute_script("arguments[0].click();", find_btn)

# 50 or 100 per page selectors
# select_page = Select(driver.find_element_by_id('MainCopy_ctl26_ResultsPerPage'))
# select_page.select_by_visible_text('50 per page')

#Function for extracting individual profile data
def profile_data(xpath) :
    #Finding profile element by Xpath
    profile = driver.find_element_by_xpath(xpath)
    driver.execute_script("arguments[0].click();", profile)

    #Extracting individual elements on profile page
    try:
        main_name = driver.find_element_by_id('MainCopy_ctl23_lblName').text
        member_name = main_name.split(",", 1)[0]
    except NoSuchElementException:
        member_name = "-"

    try:
        main_jobtitle = driver.find_element_by_id('MainCopy_ctl27_DisplayPresentJob1_JobDepartmentPanel').text
        member_jobtitle = main_jobtitle.split(",", 1)[0]
    except NoSuchElementException:
        member_jobtitle = "-"

    try:
        member_company = driver.find_element_by_id('MainCopy_ctl27_DisplayPresentJob1_CompanyNamePanel').text

    except NoSuchElementException:
        member_company = "-"

    try:
        member_mail = driver.find_element_by_id('MainCopy_ctl14_presentJob_EmailAddress').text
    except NoSuchElementException:
        member_mail = "-"

    try:
        main_phone = driver.find_element_by_id('MainCopy_ctl14_presentJob_Phone1Panel').text
        member_phone = main_phone.split('primary: ', 1)[0]
    except NoSuchElementException:
        member_phone = "-"

    try:
        main_address = driver.find_element_by_id('MainCopy_ctl14_presentJob_CityStateRegionPanel').text
        member_city = main_address.split(',', 2)[0]
    except NoSuchElementException:
        member_city="-"

    # writing all the variables from list to data.csv file
    f.write(member_name + "," + member_jobtitle+ "," + member_company + "," + member_mail + "," + member_phone + "," + "- ," + member_city + ", Maine" + "\n")

#Opening the file to save the extracted data
file_name = "data.csv"
f = open(file_name, "w")

# loop for iterating through each profile
def loopforprofile():
    for i in range(0, 9):
        #Creating xpaths for individual profile
        profile_xpath = '//*[@id="MainCopy_ctl26_Contacts_DisplayName_' + str(i) + '"]'

        #Calling profile_data() function with xpath parameter
        profile_data(profile_xpath)

        #clicking back button before another iteration
        driver.execute_script("window.history.go(-1)")

loopforprofile()

next_btn = driver.find_element_by_xpath('//*[@id="MainCopy_ctl26_Pager_NextPageButton"]')
driver.execute_script("arguments[0].click();", next_btn)

loopforprofile()

f.close()
driver.close()



