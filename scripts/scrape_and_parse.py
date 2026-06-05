from playwright.sync_api import sync_playwright
import json

URL = "https://www.fifa.com/en/tournaments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fixtures-results-teams-stadiums"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(URL)

    page.wait_for_timeout(5000)

    text = page.locator("body").inner_text()

    with open("fixtures.txt", "r", encoding="utf-8") as f:
        text = f.read()

    lines = text.splitlines()

    date_keywords = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

    current_date = None
    matches = []

    for line in lines:

        if "Round of 32 fixtures" in line:
            break

        if any(line.startswith(day) for day in date_keywords):
            current_date = line
            continue

        if " v " in line and "Group" in line:

            line = line.replace("–", "-")

            parts = line.split(" - ")

            if len(parts) != 3:
                continue

            teams = parts[0].strip()
            group = parts[1].replace("Group ", "")
            stadium = parts[2]

            home_team, away_team = teams.split(" v ")

            match = {
                "date": current_date,
                "home_team": home_team,
                "away_team": away_team,
                "group": group,
                "stadium": stadium
            }
            matches.append(match)

            with open("data/matches.json", "w", encoding="utf-8") as f:
                json.dump(matches, f, ensure_ascii=False, indent=4)


    print(f"saved {len(matches)} matches")





            


    browser.close()
    page.close()