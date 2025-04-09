from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # Đăng nhập
    driver.get("http://localhost:5173/login")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    # Vào Category Management
    category_nav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Category Management']")))
    category_nav.click()

    # Không nhập gì
    input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter category name']")))
    input_field.clear()
    input_field.send_keys("Selenium Test Category")
    # Click Add
    add_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]")
    add_button.click()

    # Chờ alert từ React
    alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
    alert_text = alert.text
    print("Popup hiển thị:", alert_text)

    if alert_text == "Unable to add/update category!":
        print("PASSED")
    else:
        print("FAILED - Nội dung thông báo không đúng mong đợi")
    alert.accept()

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    time.sleep(2)
    driver.quit()
