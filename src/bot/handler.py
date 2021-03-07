import vk_api

import random
from datetime import datetime, date, time

from loguru import logger

from .meta import TOKEN, GROUP_ID, TIMA_ID, ARTYOM_ID
from .parse import data_from_site
from .utils import (
    week_num,
    date_normolize,
    comprasion,
    messeage_create,
    comprasion_subject,
    time_normolize,
)


def postman(user_id, message):

    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    vk.messages.send(
        message=message,
        random_id=random.getrandbits(32),
        user_id=user_id,
    )

    return


# TODO: сделать проверку расписания через каждые полчаса и уведомить при изменении
def сontroller():
    date_now, week_number = week_num()
    data = data_from_site(week_number)

    for day in data:
        norm_date = date_normolize(day["day_number"])
        date_comprasion = comprasion(norm_date, date_now)

        if date_comprasion == True:
            message = ""
            for i, sub in enumerate(day["subjects"]):
                message_norm = messeage_create(sub)
                message += f"{i+1}. {message_norm}\n"

            postman(TIMA_ID, message)

            for i, sub in enumerate(day["subjects"]):
                time_lesson = sub["time"]
                time_site, time_now = time_normolize(time_lesson)
                time_site = time(time_site[0], time_site[1])
                time_now = time(time_now[0], time_now[1])
                time_different = datetime.combine(
                    date.today(), time_site
                ) - datetime.combine(date.today(), time_now)
                different = time_different.seconds // 60

            return different, day["subjects"]

        else:
            continue

        message = "Сегодня у вас пар нет"
        postman(TIMA_ID, message)
        break
