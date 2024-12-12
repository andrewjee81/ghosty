import time as tm
import schedule
from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright
from functools import partial


def run(playwright: Playwright, msg) -> None:
    try:
        browser = playwright.chromium.launch(headless=False, slow_mo=3000)
        context = browser.new_context(storage_state="discord.json")
        page = context.new_page()
        page.goto("#")
        page.wait_for_load_state("networkidle")
        page.get_by_label("Message #🎮⏐ghosty").locator("div").click()
        page.get_by_label("Message #🎮⏐ghosty").locator("div").fill(msg)
        page.get_by_label("Message #🎮⏐ghosty").press("Enter")

        print(f"Message sent at {datetime.now()}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        context.close()
        browser.close()


def job(msg):
    print(f"Job started at {datetime.now()}")
    with sync_playwright() as playwright:
        run(playwright, msg)


# Schedule the job
schedule.every().day.at("02:00").do(job, "?date")
schedule.every().day.at("02:11").do(job, "?date")
schedule.every().day.at("03:02").do(job, "?date")
schedule.every().day.at("03:22").do(job, "?date")
schedule.every().day.at("04:03").do(job, "?date")
schedule.every().day.at("04:33").do(job, "?date")
schedule.every().day.at("05:04").do(job, "?date")
schedule.every().day.at("05:44").do(job, "?date")
schedule.every().day.at("06:05").do(job, "?date")
schedule.every().day.at("06:55").do(job, "?date")
schedule.every().day.at("07:06").do(job, "?date")
schedule.every().day.at("08:07").do(job, "?date")
schedule.every().day.at("09:08").do(job, "?date")
schedule.every().day.at("10:09").do(job, "?date")
schedule.every().day.at("11:10").do(job, "?date")
schedule.every().day.at("12:11").do(job, "?date")
schedule.every().day.at("13:12").do(job, "?date")
schedule.every().day.at("13:21").do(job, "?date")
schedule.every().day.at("14:13").do(job, "?date")
schedule.every().day.at("14:31").do(job, "?date")
schedule.every().day.at("14:37").do(job, "?date")
schedule.every().day.at("15:14").do(job, "?date")
schedule.every().day.at("15:41").do(job, "?date")
schedule.every().day.at("16:15").do(job, "?date")
schedule.every().day.at("16:51").do(job, "?date")
schedule.every().day.at("17:16").do(job, "?date")
schedule.every().day.at("18:17").do(job, "?date")
schedule.every().day.at("19:18").do(job, "?date")
schedule.every().day.at("20:19").do(job, "?date")
schedule.every().day.at("21:02").do(job, "?date")
schedule.every().day.at("21:20").do(job, "?date")
schedule.every().day.at("22:12").do(job, "?date")
schedule.every().day.at("22:21").do(job, "?date")
schedule.every().day.at("23:22").do(job, "?date")
schedule.every().day.at("00:23").do(job, "?date")
schedule.every().day.at("00:32").do(job, "?date")
schedule.every().day.at("01:00").do(job, "?date")

#schedule.every(55).seconds.do(job, "?goos")

print("Scheduler is running... Press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    tm.sleep(1)
