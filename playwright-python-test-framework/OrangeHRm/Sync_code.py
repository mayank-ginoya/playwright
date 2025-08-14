import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright


async def drashti():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        await page.fill("//input[@name='username']", "Admin")
        await page.fill("//input[@name='password']", "admin123")
        await page.click("//button[@type='submit']")
        await page.wait_for_selector("//span[text()='PIM']")
        await page.screenshot(path="screenshots/login.png")
        await browser.close()


asyncio.run(drashti())
with sync_playwright() as p:
    browser =  p.chromium.launch(headless=False)
    page =  browser.new_page()
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.fill("//input[@name='username']", "Admin")
    page.fill("//input[@name='password']", "admin123")
    page.click("//button[@type='submit']")
    page.wait_for_selector("//span[text()='PIM']")
    page.screenshot(path="screenshots/login.png")
    browser.close()

