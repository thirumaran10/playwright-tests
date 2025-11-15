from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.redbus.in/', wait_until="load")
    page.wait_for_load_state("networkidle")

    #give all the cookies present in the browser
    '''my_cookies = page.context.cookies()
    print(my_cookies)

    #clear all the cookies
    page.context.clear_cookies()

    new_cookies = {
        'name': 'Mycookie1',
        'value': '1234567',
    }
    #To pass the new cookie to the browser
    page.context.add_cookies([new_cookies])'''

    #taking screenshot of the page
    page.screenshot(path='redbus_cookies.png', full_page=True)
    page.wait_for_timeout(5000)
    browser.close()
