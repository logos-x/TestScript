from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://localhost:5173/login")
    wait = WebDriverWait(driver, 10)

    # Đăng nhập
    driver.find_element(By.NAME, "email").send_keys("user@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("User-123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    # Bấm vào nút "Create Event"
    create_event_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Event List")))
    create_event_btn.click()

    wait = WebDriverWait(driver, 10)
    buttons = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//button[contains(text(), 'View Details')]")
    ))

    buttons[0].click()

    service = wait.until(EC.presence_of_element_located(
        (By.TAG_NAME, "select")
    ))
    select = Select(service)

    input_qty = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
    input_qty.clear()
    input_qty.send_keys("999")

    add_service_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Service')]")
    add_service_btn.click()

    # Kiểm tra thông báo thành công
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Thông báo từ hệ thống: {alert_text}")
    alert.accept()

    if alert_text.strip() == "Please select a service and enter a valid quantity!":
        print("PASSED")
    else:
        print("FAILED - Nội dung alert không đúng mong đợi")

    input("Nhập Enter để tiếp tục ...")
    
except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    driver.quit()
