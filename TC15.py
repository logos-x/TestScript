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

    # Nhập email hợp lệ nhưng KHÔNG nhập mật khẩu
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys("user@gmail.com")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("")  # Không nhập mật khẩu

    # Click nút Sign In
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
    sign_in_button.click()

    # Kiểm tra xem có thông báo lỗi xuất hiện không (tùy vào cách bạn show alert/toast/message)
    # Ví dụ: kiểm tra alert() từ JS
    try:
        alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"Thông báo từ hệ thống: {alert_text}")

        if alert_text.strip() == "Vui lòng nhập đầy đủ thông tin đăng nhập":
            print("PASSED")
        else:
            print("FAILED - Nội dung cảnh báo không đúng")

        alert.accept()

    except:
        try:
            message = wait.until(EC.visibility_of_element_located((
                By.XPATH, "//*[contains(text(), 'Vui lòng nhập đầy đủ thông tin đăng nhập')]"
            )))
            print("Thông báo hiển thị:", message.text)
            print("PASSED")
        except:
            print("FAILED - Không tìm thấy thông báo lỗi")

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    driver.quit()
