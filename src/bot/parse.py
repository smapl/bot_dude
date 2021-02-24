from bs4 import BeautifulSoup
from loguru import logger

import requests
import json

from .utils import edit


def data_from_site(week_number):
    url = f"https://mai.ru/education/schedule/detail.php?group=%D0%A212%D0%9E-105%D0%9C-20&week={week_number}"

    response = requests.get(url)
    schedule = list()
    soup = BeautifulSoup(response.text, "html5lib")

    content_block = soup.find("div", {"id": "schedule-content"})
    days = content_block.find_all("div", {"class": "sc-container"})

    for day in days:

        try:
            day_number = day.find(
                "div", {"class": "sc-table-col sc-day-header sc-gray"}
            ).text
        except Exception as ex:
            logger.info(ex)
            day_number = day.find(
                "div", {"class": "sc-table-col sc-day-header sc-blue"}
            ).text
        subs = day.find("div", {"class": "sc-table sc-table-detail"})
        subjects = subs.find_all("div", {"class": "sc-table-row"})

        day_subjects = list()
        for subject in subjects:

            subject_time = subject.find(
                "div", {"class": "sc-table-col sc-item-time"}
            ).text

            type_subjects = subject.find(
                "div", {"class": "sc-table-col sc-item-type"}
            ).text

            name_subject = subject.find("span", {"class": "sc-title"}).text
            lecturer = subject.find("span", {"class": "sc-lecturer"}).text
            geo = subject.find("div", class_="sc-item-location").get_text()
            geo = edit(geo)

            dict_subcject = {
                "time": subject_time,
                "type": type_subjects,
                "name": name_subject,
                "lecturer": lecturer,
                "geo": geo,
            }
            day_subjects.append(dict_subcject)

        data_day = {
            "day_number": day_number,
            "subjects": day_subjects,
        }

        schedule.append(data_day)
    return schedule