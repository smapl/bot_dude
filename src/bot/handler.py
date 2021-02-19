import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent


import random

from .meta import TOKEN, GROUP_ID

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk=vk_session, group_id=GROUP_ID)


def listener():

    vk_session = vk_api.VkApi(token=TOKEN)
    vk = vk_session.get_api()
    longpoll = VkBotLongPoll(vk=vk_session, group_id=GROUP_ID)

    for event in longpoll.listen():
        
        peer_id = event.message.peer_id
        vk.messages.send(
            message="hola",
            random_id=random.getrandbits(32),
            peer_id=peer_id,
        )

