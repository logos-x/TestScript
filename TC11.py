from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://localhost:5173/login")

    wait = WebDriverWait(driver, 10)

    # Nhập email và password
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys("nonexistent@example.com")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("wrongpassword")

    # Click nút Sign In
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
    sign_in_button.click()

    # Đợi và xử lý alert nếu xuất hiện
    try:
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Thông báo từ hệ thống: {alert_text}")

        if alert_text.strip() == "Email or password is incorrect":
            print("PASSED")
        else:
            print("FAILED - Nội dung alert không đúng mong đợi")

        alert.accept()

    except:
        print("FAILED - Không có alert xuất hiện")

finally:
    driver.quit()