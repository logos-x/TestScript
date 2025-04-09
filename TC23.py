from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import os

# Khởi tạo trình duyệt
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("http://localhost:5173/login")
    wait = WebDriverWait(driver, 10)

    # Đăng nhập
    driver.find_element(By.NAME, "email").send_keys("user@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("User-123")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

    # Bấm vào nút "Create Event"
    create_event_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Create Event")))
    create_event_btn.click()

    # Nhập thông tin sự kiện
    wait.until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Birthday Party")

    select = Select(driver.find_element(By.NAME, "category"))
    select.select_by_index(1)

    date = driver.find_element(By.NAME, "date")
    date.send_keys("01-01-2025")

    driver.find_element(By.NAME, "location").send_keys("Hồ Chí Minh")

    driver.find_element(By.NAME, "description").send_keys("Tổ chức sinh nhật tại nhà hàng ABC với bạn bè.")

    file_input = driver.find_element(By.NAME, "image")

    image_path = "asset/image_event.png"
    abs_path = os.path.abspath(image_path)
    file_input.send_keys(abs_path)

    create_btn = driver.find_element(By.XPATH, "//button[text()='Create Event']")
    create_btn.click()

    # Kiểm tra thông báo thành công
    error_msg = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'text-red-700')]"))
    )

    expected_message = "Ngày không được nằm trong quá khứ!"
    if expected_message == error_msg.text:
        print("PASSED")
    else:
        print("FAILED - Nội dung thông báo không đúng mong đợi.")

    input("Nhập Enter để tiếp tục ...")
    
except Exception as e:
    print("FAILED - Có lỗi xảy ra:", e)

finally:
    driver.quit()
