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

    # Nhập email và password hợp lệ
    email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email_input.send_keys("user1@gmail.com")

    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("User@123")

    # Click nút Sign In
    sign_in_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]")
    sign_in_button.click()

    # Đợi điều kiện thể hiện đã đăng nhập thành công
    # Ví dụ: đợi URL chuyển sang trang chủ, hoặc một element nào đó chỉ có sau khi đăng nhập
    WebDriverWait(driver, 10).until(
        EC.url_changes("http://localhost:5173/login")
    )

    # Kiểm tra xem có đang ở trang chính hay không (hoặc dashboard/admin/users tùy user)
    current_url = driver.current_url
    print("Current URL sau khi đăng nhập:", current_url)

    if "login" not in current_url:
        print("PASSED - Đăng nhập thành công và đã chuyển trang")
    else:
        print("FAILED - Vẫn ở trang login, có thể đăng nhập thất bại")

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    driver.quit()
