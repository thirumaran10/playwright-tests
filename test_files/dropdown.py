from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html", wait_until="load")

    #page.wait_for_load_state("load")   # wait until full load

    #instead of click we can use check for radio button and checkbox only
    #radio button
    page.check('//input[@value="Male"]')

    #checkbox
    page.locator('//input[@id="checkbox1"]').click()
    page.check('//input[@id="checkbox2"]')

    # page.wait_for_timeout(15000)
    # print(page.title())
    # browser.close()
    print("Page Title:", page.title())
    page.wait_for_timeout(5000)
    browser.close()
