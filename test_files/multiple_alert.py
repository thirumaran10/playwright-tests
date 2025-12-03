from playwright.sync_api import sync_playwright

text_alert = []

def handle_dialog(dialog):
    message = dialog.message
    text_alert.append(message)
    dialog.dismiss()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html")
    page.wait_for_load_state("networkidle")   # wait until full load

    #alert with OK
    page.query_selector("//a[text() = 'Alert with OK ']").click()
    #direct child of xpath use /
    #control alert
    page.once("dialog",lambda dialog: dialog.accept())
    page.locator('//div[@id="OKTab"]/button').click()

    page.locator('//a[@href="#CancelTab"]').click()

    #alert with cancel and print the text of alert
    
    page.once("dialog",handle_dialog)
    
    page.query_selector('//button[@onclick="confirmbox()"]').click()

    page.wait_for_timeout(5000)
    browser.close()
    print(text_alert[0])

