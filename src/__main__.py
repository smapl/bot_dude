import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType, VkBotMessageEvent

from .bot import handler.listener 

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk=vk_session, group_id=GROUP_ID)

if __name__ == "__main__":
    listener(longpoll, vk)