from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless = False)
    context = browser.new_context() #Creates a proper browser context
    page = context.new_page() #Creates a new page inside that context
    page.goto('https://demo.automationtesting.in/Windows.html')
    page.wait_for_load_state("networkidle")   

    page.query_selector('//a[@target="_blank"]/button').click()
    page.wait_for_timeout(5000)

    #How to find the total pages
    total_pages = context.pages
    print("Total pages are:", len(total_pages))

    #print the page objects references
    for i in total_pages: 
        print(i)

    new_page = total_pages[1] # storing the new page reference
    page.wait_for_timeout(2000)
    
    #switch to new page 
    new_page.bring_to_front()
    print("New page title is:", new_page.title())
    new_page.close() # its only close current tab

