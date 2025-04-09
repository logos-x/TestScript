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

    # Ghi đè window.alert để lưu nội dung alert vào biến toàn cục
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

    # Vào trang Category Management
    category_nav = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Category Management']")))
    category_nav.click()

    # Chờ danh sách categories hiện ra
    wait.until(EC.presence_of_element_located((By.XPATH, "//ul/li")))

    # Bấm nút Edit trên category đầu tiên
    edit_button = driver.find_element(By.XPATH, "(//button[text()='Edit'])[1]")
    edit_button.click()

    # Xóa nội dung cũ, nhập tên đã tồn tại: Selenium Test Category
    input_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter category name']")))
    input_field.clear()
    input_field.send_keys("Selenium Test Category")

    # Bấm nút Update
    update_button = driver.find_element(By.XPATH, "//button[text()='Update']")
    update_button.click()

    # Đợi React gọi alert và lấy nội dung
    time.sleep(1)
    alert_text = driver.execute_script("return window.__lastAlertMessage;")
    print("Popup hiển thị:", alert_text)

    if alert_text == "Unable to add/update category!":
        print("PASSED")
    else:
        print("FAILED - Không đúng nội dung thông báo mong đợi.")

except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    time.sleep(2)
    driver.quit()