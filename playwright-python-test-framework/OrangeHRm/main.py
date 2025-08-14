import asyncio
from playwright.async_api import async_playwright
from orangehrm_modules import (
    login,
    navigate_pim_add_employee,
    navigate_time_module,
    navigate_attendance_module,
    navigate_admin_module,
    navigate_job_module_add_job
)

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await login(page)
        await navigate_pim_add_employee(page)
        await navigate_time_module(page)
        await navigate_attendance_module(page)
        await navigate_admin_module(page)
        # await navigate_job_module_add_job(page)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
