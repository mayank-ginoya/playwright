from playwright.async_api import Page

async def login(page: Page):
    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    await page.fill("//input[@name='username']", "Admin")
    await page.fill("//input[@name='password']", "admin123")
    await page.click("//button[@type='submit']")
    await page.wait_for_selector("//span[text()='PIM']")
    await page.screenshot(path="screenshots/login.png")

async def navigate_pim_add_employee(page: Page):
    await page.click("//span[text()='PIM']")
    await page.wait_for_selector("//a[text()='Add Employee']")
    await page.click("//a[text()='Add Employee']")
    await page.wait_for_selector("//input[@placeholder='First Name']")
    await page.fill("//input[@placeholder='First Name']", "mayank")
    await page.fill("//input[@placeholder='Last Name']", "drashti")
    await page.click("//button[@type='submit']")
    await page.wait_for_selector("//span[text()='PIM']")
    await page.screenshot(path="screenshots/pim_add_employee.png")

async def navigate_time_module(page: Page):
    await page.click("//span[text()='Time']")
    await page.wait_for_selector("//input[@placeholder='Type for hints...']")
    await page.fill("//input[@placeholder='Type for hints...']", "Test")
    await page.click("//div[@role='listbox']")
    await page.click("//button[@type='submit']")
    await page.screenshot(path="screenshots/time_module.png")

async def navigate_attendance_module(page: Page):
    await page.click("//span[text()='Attendance ']")
    await page.wait_for_selector("//a[text()='My Records']")
    await page.click("//a[text()='My Records']")
    # await page.wait_for_selector("//i[@class='oxd-icon bi-caret-down-fill']")
    # await page.click("//i[@class='oxd-icon bi-caret-down-fill']")
    await page.fill("//input[@placeholder='yyyy-dd-mm']", "")
    await page.fill("//input[@placeholder='yyyy-dd-mm']", "2025-10-07")
    await page.click("//button[@type='submit']")
    await page.click("//i[@class='oxd-icon bi-calendar oxd-date-input-icon']")
    await page.screenshot(path="screenshots/attendance_module.png")

async def navigate_admin_module(page: Page):
    await page.click("//span[text()='Admin']")
    await page.wait_for_selector("//div[@class='oxd-topbar-header-title']", timeout=5000)
    button = page.locator(".oxd-select-text-input").nth(0)
    await button.click()
    button =  page.locator("text=ESS")
    await button.click()
    button = page.locator(".oxd-select-text-input").nth(1)
    await button.click()
    button = page.locator("text=Disabled")
    await button.click()
    await page.wait_for_timeout(2000)
    await page.screenshot(path="screenshots/admin_module.png")

async def navigate_job_module_add_job(page: Page):
    await page.click("//span[text()='Job ']")
    await page.wait_for_selector("//a[text()='Job Titles']")
    await page.click("//a[text()='Job Titles']")
    await page.wait_for_selector("//i[@class='oxd-icon bi-plus oxd-button-icon']")
    await page.click("//i[@class='oxd-icon bi-plus oxd-button-icon']")
    await page.wait_for_selector("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    await page.fill("//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']", "testingmethodscycle1")
    await page.fill("//textarea[@placeholder='Type description here']", "At Nutanix Cloud Manager, we are trying to build the next generation platform to help enterprises model, develop and manage applications. ")
    await page.fill("//textarea[@placeholder='Add note']", "At Nutanix Cloud Manager. ")
    file_input = page.locator("input[type='file']")
    await file_input.set_input_files("C:/Users/KHODIYAR/Downloads/OrangeHRM.txt")
    await page.click("//button[@type='submit']")
    await page.screenshot(path="screenshots/job_add_job.png")
