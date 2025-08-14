import asyncio
from playwright.async_api import async_playwright

from OrangeHRm.functionOrangeHRM import *


async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        # Login
        page = await login_orange(page)
        # Wait for dashboard to load (wait for PIM menu to be visible)
        page = await pim_details(page)



        await browser.close()

asyncio.run(run())
