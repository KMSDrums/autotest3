from playwright.sync_api import sync_playwright
import data

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        email = data.email()
        password = data.password()
        browser = browser_type.launch(headless=False)
        print(browser_type.name, 'test started')
        page = browser.new_page(locale='en-GB')
        page.goto("https://int.dev.clusters.cyber.bet/")
        # Login
        page.click('text=Log in')
        page.type("input[name='email']", email)
        page.type("input[name='password']", password)
        page.click('text=Log in')
        # Select tournament
        page.click('text=Football')
        page.wait_for_timeout(3000)
        page.click("xpath=//*[@id='game-filter-wrapper']/div[6]/div/div[2]/div[1]/button")
        page.wait_for_timeout(2000)
        # Add to favorites
        page.click("xpath=//*[@id='game-filter-wrapper']/div[6]/div/div[2]/div[2]/button")
        page.wait_for_timeout(3000)

        # Check favorites
        check_visibility = page.is_visible("xpath=//*[@id='main-content']/div[1]/div/div[1]/div/div[1]/div[2]/div[2]")
        if check_visibility:
            print('Success')
        # Delete tournament from Favorites
        page.click("xpath=//*[@id='main-content']/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/button")
        browser.close()
        print('Test finished')
    print('All tests are finished')
