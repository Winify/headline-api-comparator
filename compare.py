#!/usr/bin/python
import csv

from load_headlines import headlines
from tester_apis.automizy import automizy_api_score
from tester_apis.co_schedule import co_schedule_selenium_score
from tester_apis.net_atlantic import net_atlantic_selenium_score
from tester_apis.spamcheck_postmark import spamcheck_api_score
from utils.open_browser import driver
from utils.progress_bar import progress
from utils.selenium_helper import current_time

result_file = 'out/result_{}.csv'.format(current_time)
first_query = True

try:
    with open(result_file, 'w', newline='') as result:
        writer = csv.writer(result, delimiter=',')
        writer.writerow(
            ['headline', ' automizy_score', ' send_checkit_score', ' co_schedule_score', ' net_atlantic_score',
             ' spamcheck_score'])

        for headline in progress(headlines):
            automizy_score = automizy_api_score("phraseScoreEstimator", headline)
            send_checkit_score = automizy_api_score("coScheduleScoreScraper", headline)
            co_schedule_score = co_schedule_selenium_score(first_query, headline)
            net_atlantic_score = net_atlantic_selenium_score(headline)
            spamcheck_score = spamcheck_api_score(headline)

            first_query = False
            writer.writerow(
                [headline, automizy_score, send_checkit_score, co_schedule_score, net_atlantic_score, spamcheck_score])
finally:
    progress.finish()
    driver.quit()
