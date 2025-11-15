#launch browser and create context and page using conftest fixture and verify page title
import pytest
from playwright.sync_api import sync_playwright

def test_google(page):  # lowercase name
    page.goto("https://www.google.com")
    assert "Google" in page.title()
    print(" Google test passed")

def test_orangehrm(page):  # lowercase name
    page.goto("https://www.orangehrm.com/")
    assert "OrangeHRM" in page.title()
    print(" OrangeHRM test passed")
