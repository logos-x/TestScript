from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # B1: Mở trang login
    driver.get("http://localhost:5173/login")
    wait = WebDriverWait(driver, 10)

    # B2: Đăng nhập
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    # B3: Truy cập Category Management
    category_nav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Category Management']")))
    category_nav.click()

    # B4: Chờ danh sách hiện ra
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul")))

    # B5: Click nút Edit ở category đầu tiên (hoặc bạn có thể dùng text cụ thể nếu muốn)
    first_edit_button = driver.find_element(By.XPATH, "//button[text()='Edit']")
    first_edit_button.click()

    # B6: Chỉnh sửa nội dung Category Name
    input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter category name']")))
    input_field.clear()
    input_field.send_keys("Đám hỏi")

    # B7: Click nút Update
    update_button = driver.find_element(By.XPATH, "//button[text()='Update']")
    update_button.click()

    # B8: Chờ alert hiện lên từ `alert(...)`
    alert = WebDriverWait(driver, 3).until(EC.alert_is_present())
    alert_text = alert.text
    print("Popup hiển thị:", alert_text)

    if alert_text == "Category updated successfully!":
        print("PASSED")
    else:
        print("FAILED - Nội dung thông báo không đúng.")
    alert.accept()

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    time.sleep(2)
    driver.quit()
