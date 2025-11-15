import pytest
from playwright.sync_api import sync_playwright


class TestTitle:
    def test_google(self,page): 
        page.goto("https://www.google.com") 
        assert page.url == "https://www.google.com/" 

    def test_orange(self,page):
        page.goto("https://www.orangehrm.com/") 
        assert page.url == "https://www.orangehrm.com/" 
        
