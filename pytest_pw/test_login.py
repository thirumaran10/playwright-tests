import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.parametrize("invalid_username, invalid_password",[("Admin", "admin1234"), (" ad", "12 "),("Admin", "admin123")])
def test_invalid_login(page, invalid_username, invalid_password):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until="load")

    page.fill('//input[@name="username"]',invalid_username)  # invalid username
    page.fill('//input[@name="password"]',invalid_password)  # invalid password
    page.click('//button[@type="submit"]')

    page.wait_for_timeout(3000)  # wait for 3 seconds to
    error_message = page.wait_for_selector('//div[@role="alert"]//p').text_content()
    assert "Invalid credentials" in error_message
