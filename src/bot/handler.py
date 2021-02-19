import vk_api

import random
import datetime

from loguru import logger

from .meta import TOKEN, GROUP_ID
from .parse import data_from_site
from .utils import week_num, date_normolize, comprasion, messeage_create


def postman(user_id, message):

    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    vk.messages.send(
        message=message,
        random_id=random.getrandbits(32),
        user_id=user_id,
    )

    return


def сontroller():
    user_id = "211217307"
    date_now, week_number = week_num()
    data = data_from_site(week_number)

    for day in data:
        norm_date = date_normolize(day["day_number"])
        date_comprasion = comprasion(norm_date, date_now)

        if date_comprasion == True:
            message = messeage_create(day["subjects"])
            postman(user_id, message)

            return True

        else:
            continue

    return False
