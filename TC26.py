from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)

    # Truy cập trang đăng nhập và ghi đè window.alert để lấy thông báo sau này
    driver.get("http://localhost:5173/login")
    driver.execute_script("""
        window.__lastAlertMessage = "";
        window.alert = function(msg) {
            window.__lastAlertMessage = msg;
        };
    """)

    # Đăng nhập
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    # Truy cập "Service Management"
    service_nav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Service Management']")))
    service_nav.click()

    # Chờ form xuất hiện
    wait.until(EC.presence_of_element_located((By.XPATH, "//form")))

    # Nhập dữ liệu
    driver.find_element(By.XPATH, "//input[@placeholder='Enter service name']").send_keys("Service A")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter quantity']").send_keys("2")
    driver.find_element(By.XPATH, "//textarea[@placeholder='Enter service description']").send_keys("Không có")
    driver.find_element(By.XPATH, "//input[@placeholder='Enter price']").send_keys("8000000")

    # Nhấn nút Add
    driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]").click()

    # Đợi và lấy thông báo alert
    time.sleep(1)
    alert_text = driver.execute_script("return window.__lastAlertMessage;")
    print("Popup hiển thị:", alert_text)

    if alert_text == "Service added successfully!":
        print("PASSED")
    else:
        print("FAILED - Không đúng nội dung thông báo mong đợi.")

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    time.sleep(2)
    driver.quit()
