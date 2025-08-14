#to run this, just: pytest -> https://playwright.dev/python/docs/test-runners
#pytest --headed
#pytest --browser chromium --browser webkit
#pytest --base-url https://www.saucedemo.com/ --browser chromium --headed
#Run tests with slow mo with the --slowmo argument.: --slowmo 1000 


#Configure Mypy typings for auto-completion
# from playwright.sync_api import Page
from playwright.async_api import Page
import pytest

from OrangeHRm.orangehrm_modules import *


#--Skip test by browser
#@pytest.mark.skip_browser("firefox")
#--Run on a specific browser
#@pytest.mark.only_browser("chromium")
def test_example_is_working(page: Page):
    page.goto("/")
    assert page.inner_text('title') == 'Swag Labs'


def test_example_is_working_async(page: Page):
    page.goto("/")
    login(page)
    navigate_pim_add_employee(page)
    navigate_time_module(page)
    navigate_attendance_module(page)
    navigate_admin_module(page)
    # await navigate_job_module_add_job(page)


    