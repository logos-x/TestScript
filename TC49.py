from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    wait = WebDriverWait(driver, 10)

    # 1. Đăng nhập
    driver.get("http://localhost:5173/login")
    wait.until(EC.presence_of_element_located((By.NAME, "email"))).send_keys("admin@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Admin@123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    # 2. Vào trang Event Management
    event_nav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Event Management']")))
    event_nav.click()

    # 3. Đợi danh sách sự kiện hiển thị, rồi click "View Details" của event đầu tiên

    wait = WebDriverWait(driver, 10)
    buttons = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//button[contains(text(), 'View Details')]")
    ))

    buttons[0].click()

    trash_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "svg.lucide-trash2"))
    )
    trash_icon.click()

    confirm = driver.switch_to.alert
    confirm.accept()

    # Kiểm tra thông báo thành công
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Thông báo từ hệ thống: {alert_text}")
    alert.accept()

    if alert_text.strip() == "Service removed successfully!":
        print("PASSED")
    else:
        print("FAILED - Nội dung alert không đúng mong đợi")

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    time.sleep(2)
    driver.quit()
