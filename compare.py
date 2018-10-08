#!/usr/bin/python
import csv

from load_headlines import headlines
from utils.open_browser import driver
from utils.progress_bar import progress
from utils.request_helper import get_api_score
from utils.selenium_helper import current_time, get_selenium_score

result_file = 'out/result_{}.csv'.format(current_time)
first_query = True

try:
    with open(result_file, 'w', newline='') as result:
        writer = csv.writer(result, delimiter=',')
        driver.get('https://coschedule.com/headline-analyzer')

        for headline in progress(headlines):
            automizy_score = get_api_score("phraseScoreEstimator", headline)
            send_checkit_score = get_api_score("coScheduleScoreScraper", headline)
            co_schedule_score = get_selenium_score(first_query, headline)

            first_query = False
            writer.writerow([headline, automizy_score, send_checkit_score, co_schedule_score])
finally:
    progress.finish()
    driver.quit()
