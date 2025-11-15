from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_load_state("networkidle")
    
    #mouse actions to hover on menu
    #hover the dropdown menu
    page.wait_for_selector('//a[text() = "SwitchTo"]').hover()
    #click on element
    page.wait_for_selector('//a[text() = "Windows"]').click()
    #Double click on element
    page.wait_for_selector('//button[@onclick="newwindow()"]').dblclick()
    #Right click on element
    page.wait_for_selector('//button[@onclick="newwindow()"]').click(button="right")
    #shift click on element
    page.wait_for_selector('//button[@onclick="newwindow()"]').click(modifiers=["Shift"])

    #keyboard actions
    #pressing keys
    page.wait_for_selector('//a[text() = "SwitchTo"]').press("ArrowDown")
    #A-Z, 0-9,F1-F12, Arrow keys, Escape, Enter, Tab, Backspace, Delete, Insert, Home, End, PageUp, PageDown
    page.wait_for_selector('//a[text() = "SwitchTo"]').press("F4")
    #dollar sign ($), caret (^), plus (+), and tilde (~) characters
    page.wait_for_selector('//a[text() = "SwitchTo"]').press("+")
    #combination of keys
    page.wait_for_selector('//a[text() = "SwitchTo"]').press("Control+A")

    page.wait_for_timeout(5000)

