from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)

    # Truy cập trang login
    driver.get("http://localhost:5173/login")
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    # Vào Service Management
    service_nav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Service Management']")))
    service_nav.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul/li")))

    # Edit dịch vụ đầu tiên
    edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Edit'])[1]")))
    edit_button.click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))

    # Override window.alert để bắt thông báo
    driver.execute_script("""
        window.__lastAlertMessage = null;
        window.alert = function(msg) { window.__lastAlertMessage = msg; };
    """)

    # Điền Service Name = "Service A" (giả sử đã tồn tại)
    name_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter service name']")
    name_input.click()
    name_input.send_keys(Keys.CONTROL + "a")  # Chọn toàn bộ
    name_input.send_keys(Keys.BACKSPACE)      # Xóa
    name_input.send_keys("Service A")         # ten dịch vụ đã tồn tại

    # Submit form
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Update') or contains(text(), 'Add')]")
    submit_button.click()

    time.sleep(1)

    # Lấy nội dung popup
    alert_text = driver.execute_script("return window.__lastAlertMessage;")
    print("Popup hiển thị:", alert_text)

    if alert_text == "Unable to add/update service!":
        print("PASSED")
    else:
        print("FAILED - Không đúng thông báo mong đợi.")

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    time.sleep(2)
    driver.quit()
