import vk_api

import random
import datetime

from loguru import logger

from .meta import TOKEN, GROUP_ID
from .parse import data_from_site
from .utils import week_num

user_id = "108832239"


def postman():

    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk=vk_session, group_id=GROUP_ID)
    vk.messages.send(
        message="hola",
        random_id=random.getrandbits(32),
        user_id=user_id,
    )

    return


def сontroller():
    week_number = week_num()
    data = data_from_site(week_number)

    return
