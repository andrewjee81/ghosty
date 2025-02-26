# ghosty 

This script automates sending scheduled messages to a specific Discord channel using Playwright. The script runs continuously, executing predefined tasks at specific times throughout the day.

## Motivation
As part of my Python learning experience, I wanted to try my hand at basic automation. I came across a YouTube video tutorial for Playwright and knew I had to try it for the Ghosty `?date` command. Typically, Playwright is used for testing, but it works perfectly for my purpose.

## Features
- Uses Playwright to interact with the Discord web interface.
- Sends scheduled messages at predefined times.
- Handles browser context using a stored session (`discord.json`).
- Implements error handling for robustness.

## Requirements
Ensure you have the following installed:

- Python 3.x
- Playwright
- Schedule library

### Install Dependencies
```sh
pip install playwright schedule
playwright install
```

## Configuration
Modify the script to fit your specific needs:
- **Storage State**: Ensure you have a valid `discord.json` file for authentication.
- **Target Channel**: Update the locator `Message #🎮⏐ghosty` to match the exact label of the Discord channel.
- **Scheduled Times**: Adjust the `schedule.every().day.at("HH:MM").do(job, "?date")` lines to your desired times.

## Usage
Run the script using:
```sh
python script.py
```
The scheduler will execute jobs at the predefined times. The script runs indefinitely until stopped manually.

## Notes
- The script must be running in order for scheduled jobs to execute.
- The browser runs in **non-headless mode** (`headless=False`) for debugging. Change this to `True` for silent execution.
- Ensure Discord’s UI structure remains unchanged, as locators depend on it.

## Troubleshooting
- If the script fails to send messages, check for:
  - Expired or invalid `discord.json` (Re-authenticate and save a new one).
  - Discord UI changes affecting the element selectors.
  - Internet connectivity issues.

## Disclaimer
This script automates interactions with Discord and should comply with Discord’s terms of service. Use responsibly.

