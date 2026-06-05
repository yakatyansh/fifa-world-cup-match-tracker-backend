from playwright.sync_api import sync_playwright

URL = "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(URL)

    page.wait_for_timeout(5000)

    text = page.locator("body").inner_text()

    with open("fixtures.txt", "w", encoding="utf-8") as f:
        f.write(text)