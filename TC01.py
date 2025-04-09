from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://localhost:5173/register")

    wait = WebDriverWait(driver, 10)

    # Nhập username, email và password
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    email_input.send_keys("vinhuser")

    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys("vinhuser@gmail.com")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("Vinh@123")

    # Click nút Create Account
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account')]")
    sign_in_button.click()

    # Đợi và xử lý alert nếu xuất hiện
    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Thông báo từ hệ thống: {alert_text}")
        alert.accept()

        # Đợi đến khi URL đổi sang trang login
        current_url = driver.current_url
        print(f"URL hiện tại: {current_url}")

        if alert_text.strip() == "Registration successful" and current_url == "http://localhost:5173/login":
            print("PASSED")
        else:
            print("FAILED - Nội dung alert không đúng mong đợi")

    except:
        print("FAILED - Không có alert xuất hiện")


    input("Nhấn Enter để tiếp tục...")
finally:
    driver.quit()