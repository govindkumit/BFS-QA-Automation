from playwright.sync_api import sync_playwright


def test_banking_api_documentation():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto("http://127.0.0.1:8000/docs")

        page.wait_for_load_state("networkidle")

        assert "BFS Mini Banking API" in page.locator("body").inner_text()

        browser.close()