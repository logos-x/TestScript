from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # B1: Truy cập trang đăng nhập
    driver.get("http://localhost:5173/login")
    wait = WebDriverWait(driver, 10)

    # B2: Điền email và mật khẩu admin
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    # B3: Truy cập trang Category Management
    category_nav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Category Management']")))
    category_nav.click()

    # B4: Nhập tên category mới
    input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter category name']")))
    new_category_name = "Selenium Test Category 2"
    input_field.clear()
    input_field.send_keys(new_category_name)

    # B5: Click nút Add
    add_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]")
    add_button.click()

    # B6: Chờ alert hiện ra
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text

    print("Thông báo hiển thị:", alert_text)

    if alert_text.strip() == "Category added successfully!":
        print("PASSED - Thêm category thành công.")
    else:
        print("FAILED - Nội dung thông báo sai hoặc thêm thất bại.")

    alert.accept()

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    time.sleep(2)
    driver.quit()
