from playwright.sync_api import sync_playwright

with sync_playwright() as pw:
    print("Playwright está funcionando!")
