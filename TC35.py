from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Mở trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)

    # Truy cập trang login
    driver.get("http://localhost:5173/login")

    # Đăng nhập
    # Xem coi có lỗi cú pháp gì không
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    # Truy cập trang Service Management
    service_nav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Service Management']")))
    service_nav.click()

    # Đợi danh sách dịch vụ xuất hiện
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul/li")))

    # Click nút Edit của dịch vụ đầu tiên
    edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Edit'])[1]")))
    edit_button.click()

    # Đợi form xuất hiện
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

    # Ghi đè window.alert để capture nội dung popup
    driver.execute_script("""
        window.__lastAlertMessage = null;
        window.alert = function(msg) { window.__lastAlertMessage = msg; };
    """)

    # Xóa nội dung ô Service Name
    name_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter service name']")
    name_input.clear()
    name_input.send_keys(" ")  # Gửi space

    # Bấm nút submit ("Update" hoặc "Add")
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Update') or contains(text(), 'Add')]")
    submit_button.click()

    time.sleep(1)  # Đợi alert gọi

    # Lấy nội dung từ alert override
    alert_text = driver.execute_script("return window.__lastAlertMessage;")
    print("Popup hiển thị:", alert_text)

    if alert_text == "Please fill out this field":
        print("PASSED")
    else:
        print("FAILED - Không đúng thông báo mong đợi.")
except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    time.sleep(2)
    driver.quit()
