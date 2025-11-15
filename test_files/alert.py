from playwright.sync_api import sync_playwright

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
    page.query_selector('//div[@id="OKTab"]/button').click()

    page.query_selector('//a[@href="#CancelTab"]').click()

    #alert with cancel and print the text of alert
    
    page.once("dialog",lambda dialog : (print("Alert with pressed button:", dialog.message), 
                                        dialog.dismiss(), print("Alert cancelled")))
    
    page.query_selector('//button[@onclick="confirmbox()"]').click()

    page.query_selector('//a[@href="#Textbox"]').click()
    page.query_selector('//button[@onclick="promptbox()"]').click()
    #alert with textbox
    page.once("dialog",lambda dialog : dialog.text == "TestUser" and dialog.accept())

    page.wait_for_timeout(5000)
    browser.close()


