# Exception handling and storing element in list
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
        
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    try:
        page.goto("https://demo.automationtesting.in/Selectable.html")

        #storing multiple elements in list
        elements = page.query_selector_all('b')
        print(len(elements))

        for i in elements:
            print(i.text_content())
        page.wait_for_timeout(5000)

        #intentionally causing an exception
        page.locator('//a[@href="#/Link1"]').click()

        #getting all the links in a page, query_selector was cant able to use directly using variable only it can be used
        elements = page.query_selector_all('a')
        print("Total links are:", len(elements))

        for i in elements:
            print(i.get_attribute('href'))
        page.wait_for_timeout(5000)
        

    except Exception as e:
        print("Exception occurred:", str(e))
    finally:
        print("Execution completed.") 
        
