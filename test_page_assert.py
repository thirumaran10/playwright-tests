import pytest
from playwright.sync_api import sync_playwright

def test_goto_google(page):
    page.goto("https://www.google.com", wait_until="load")
    assert "Google" in page.title()

def test_goto_orangehrm(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until="load")
    assert "OrangeHRM" in page.title()
    page.wait_for_timeout(5000)  # Wait for 5 seconds to see the page