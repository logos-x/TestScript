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
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_input.send_keys("")

    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys("user9@gmail.com")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("User9@123")

    # Click nút Create Account
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Account')]")
    sign_in_button.click()

    # Đợi và xử lý alert nếu xuất hiện
    try:
        message = driver.execute_script("return arguments[0].validationMessage;", username_input)

        expected_message = "Vui lòng điền vào trường này."

        if expected_message == message:
            print("PASSED")
        else:
            print(f"FAILED - Nội dung thông báo không đúng mong đợi.")

    except:
        print("FAILED - Không có thông báo lỗi xuất hiện")


    input("Nhấn Enter để tiếp tục...")
finally:
    driver.quit()