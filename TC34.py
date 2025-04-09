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

    # Truy cập trang đăng nhập và override alert
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

    # Đợi danh sách dịch vụ xuất hiện (ul > li)
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul/li")))

    # Tìm nút Edit đầu tiên và click
    edit_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "(//button[text()='Edit'])[1]")
    ))
    edit_button.click()

    # Đợi form xuất hiện
    wait.until(EC.presence_of_element_located((By.XPATH, "//form")))

    # Ghi đè các input
    name_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter service name']")
    name_input.clear()
    name_input.send_keys("Service B")

    qty_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter quantity']")
    qty_input.clear()
    qty_input.send_keys("3")

    desc_input = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter service description']")
    desc_input.clear()
    desc_input.send_keys("Đã có")

    price_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter price']")
    price_input.clear()
    price_input.send_keys("9000000")

    # Nhấn nút Update
    update_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Update')]")
    update_btn.click()

    # Đợi alert được override và in ra
    time.sleep(1)
    alert_text = driver.execute_script("return window.__lastAlertMessage;")
    print("Popup hiển thị:", alert_text)

    if alert_text == "Service updated successfully!":
        print("PASSED")
    else:
        print("FAILED - Không đúng thông báo mong đợi.")

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    time.sleep(2)
    driver.quit()
