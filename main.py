import requests
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from jobbot import *
import hooks

# google sheets setup
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentialjobbot.json", scope)
client = gspread.authorize(creds)

# Sheets
i_sheet = client.open("Job Opportunities 2025-2026").worksheet("Internships")
ft_sheet= client.open("Job Opportunities 2025-2026").worksheet("Full Time")

# iterates through a google sheet and posts to the given hook
def process_sheet(sheet, hook, bot: JobBot):
    all_rows = sheet.get_all_records()
    for i, row in enumerate(all_rows, start=2):  # row 1 header
        if not row.get("Posted"):
            msg = bot.msg_job(
                row.get("Title"),
                row.get("Company"),
                row.get("Employment Type"),
                row.get("Cycle"),
                row.get("Description"),
                row.get("Link"),
                row.get("Deadline")
            )
            # post to slack
            bot.post_msg(hook, msg)

            # mark as posted
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sheet.update_cell(i, 9, timestamp)
            # 9 is column i, where the 'posted' note is

if __name__ == "__main__":
    jb = JobBot()
    process_sheet(i_sheet, hooks.TEST_HOOK, jb)
    print('main complete')
