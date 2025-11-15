import pytest
from playwright.sync_api import sync_playwright

def test_login(page):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login', wait_until="load")
    assert page.title() == "OrangeHRM"
    

