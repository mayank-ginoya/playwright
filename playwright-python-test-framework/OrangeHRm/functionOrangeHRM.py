from playwright.async_api import Page

async def login_orange(page: Page) -> Page:
    # Open URL
    await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Enter username
    await page.fill("//input[@name='username']", "Admin")

    # Enter password
    await page.fill("//input[@name='password']", "admin123")

    # Take screenshot
    await page.screenshot(path='screenshot/Login.png')

    # Click LOGIN button
    await page.click("//button[@type='submit']")

    # Optionally wait for dashboard to ensure login succeeded:
    await page.wait_for_selector("//span[text()='PIM']")

    return page


async def pim_details(page):
    await page.wait_for_selector("//span[text()='PIM']")

    # Click PIM
    await page.click("//span[text()='PIM']")

    # Wait for "Add Employee" link to be visible
    await page.wait_for_selector("//a[text()='Add Employee']")
    await page.click("//a[text()='Add Employee']")

    # Wait for the Add Employee form
    await page.wait_for_selector("//input[@placeholder='First Name']")

    # Fill form
    await page.fill("//input[@placeholder='First Name']", "mayank")
    await page.fill("//input[@placeholder='Last Name']", "drashti")
    await page.screenshot(path='screenshot/PIM_userdetails.png')

    await page.click("//button[@type='submit']")
    return page