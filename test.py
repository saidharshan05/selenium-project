from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from time import sleep
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


chrome_options = Options()
chrome_options.add_argument('--headless=new')
chrome_options.platform_name = 'any'
chrome_options.add_argument("start-maximized")



# Initialize the WebDriver properly
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
page_source = driver.page_source.lower()



#testcase Login
driver.get("https://www.demoblaze.com/")
driver.find_element(By.XPATH, "//*[@id='narvbarx']//a[@id='login2']").click()
driver.find_element(By.ID, "loginusername").send_keys("qualitytesting")
driver.find_element(By.ID,"loginpassword").send_keys("test")
Loginmodel = driver.find_element(By.XPATH, '//div[@id="logInModal"]//button[contains(text(), "Log in")]')
Loginmodel.click()
wait.until(EC.invisibility_of_element(Loginmodel))
title = driver.title
assert title == 'STORE', "Title Not matched"
print("The title of the page is: ", driver.title)



#select category
laptops_button = driver.find_element(By.XPATH, "//a[@id='itemc' and contains(text(), 'Laptops')]")
laptops_button.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tbodyid")))

# Execute JavaScript to check which category was triggered 
category_loaded = driver.execute_script("return arguments[0].getAttribute('onclick');", laptops_button)

# Extract category from the onclick attribute 
expected_category = "notebook" 

# Extract 'notebook' from "byCat('notebook')"
actual_category = category_loaded.split("'")[1] 

# Verify if the correct category is loaded
assert expected_category == actual_category, f"Expected '{expected_category}', but got '{actual_category}'"
sleep(2)
wait.until(EC.visibility_of(driver.find_element(By.XPATH, "//*[@id='tbodyid']//img")))
try:
    parent_div = driver.find_element(By.ID, "tbodyid")  
    div_content = parent_div.get_attribute("innerText").lower()  

    if not "phone" in div_content:
        print("✅ The laptop filter successfully applied")
    else:
        print("❌ The string 'phone' is present in the div and its children.")

except NoSuchElementException:
    print("⚠️ The specified div was not found.")
driver.save_screenshot("./laptopfilter.png")



# Navigate to about page
try:
    driver.find_element(By.XPATH, "//li[@class='nav-item']/a[contains(text(), 'About us')]").click()
    sleep(1)
    about_title = driver.find_element(By.ID, "videoModalLabel")
    if about_title.is_displayed():
        print(f"✅ About section found")
    else:
        print("❌ About section not visible")

except NoSuchElementException:
    print("⚠️ The specified div was not found.")
driver.save_screenshot("./about.png")
driver.find_element(By.XPATH, "//*[@id='videoModal']//button").click()


# Navigate to Contact page
try:
    driver.find_element(By.XPATH, "//li[@class='nav-item']/a[contains(text(), 'Contact')]").click()
    sleep(1)
    about_title = driver.find_element(By.ID, "exampleModalLabel")
    if about_title.is_displayed():
        print(f"✅ contact section found")
    else:
        print("❌ contact section not visible")

except NoSuchElementException:
    print("⚠️ The specified div was not found.")
driver.save_screenshot("./ContactModel.png")



#Fill the contact form
def Fill_the_contact_form():
    try:
        driver.find_element(By.ID, "recipient-email").send_keys("text@example.com")
        driver.find_element(By.ID, "recipient-name").send_keys("Test User")
        driver.find_element(By.ID, "message-text").send_keys("This is a test message.")
        print("✅ Contact form filled successfully!")
    except NoSuchElementException as e:
        print(f"⚠️ Could not fill the form: {e}")
    driver.save_screenshot("./Contact.png")

Fill_the_contact_form()


driver.find_element(By.XPATH, "//*[@id='exampleModal']//button[contains(text(), 'Send message')]").click()

# Accept the alert
try:
    WebDriverWait(driver, 4).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept() 
    print("✅ Alert accepted successfully!")

except NoAlertPresentException:
        print("❌ No alert was present after form submission.")


#select category
laptops_button = driver.find_element(By.XPATH, "//a[@id='itemc' and contains(text(), 'Monitors')]")
laptops_button.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "tbodyid")))
category_loaded = driver.execute_script("return arguments[0].getAttribute('onclick');", laptops_button)
expected_category = "monitor" 
actual_category = category_loaded.split("'")[1] 


# Verify if the correct category is loaded
assert expected_category == actual_category, f"Expected '{expected_category}', but got '{actual_category}'"
sleep(2)
wait.until(EC.visibility_of(driver.find_element(By.XPATH, "//*[@id='tbodyid']//img")))
try:
    parent_div = driver.find_element(By.ID, "tbodyid")  
    div_content = parent_div.get_attribute("innerText").lower()  

    if not "phone" in div_content or "notebook" in div_content:
        print("✅ The Monitor filter successfully applied")
    else:
        print("❌ The string 'phone' & 'notebook' is present in the div and its children.")

except NoSuchElementException:
    print("⚠️ The specified div was not found.")
driver.save_screenshot("./monitorfilter.png")


#select cart section

driver.find_element(By.XPATH, "//*[@id='navbarExample']//a[contains(text(), 'Cart')]").click()
try:
    cart_title = driver.find_element(By.ID, "page-wrapper")
    if cart_title.is_displayed():
        print(f"✅ Cart section found")
    else:
        print("❌ Cart section not visible")
except NoSuchElementException:
    print("⚠️ The specified div was not found.")
driver.save_screenshot("./Cart.png")












driver.quit()