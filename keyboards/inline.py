from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kerosene", url="https://youtu.be/3biiZ0O-lBU?si=7taXYMeUrX3uYHBK"),
            InlineKeyboardButton(text="Ur final message", url="https://youtu.be/AeyTNMJ6Qss?si=yskVM397C0Ebvhkw"),
            InlineKeyboardButton(text="Lovely Bastard", url="https://youtu.be/5XK4vuB5ffk?si=nL1uDly2tGRkfwbK"),
            InlineKeyboardButton(text="Просто", url="https://youtu.be/3-Oba76JW8I?si=6yVAXbkyUfu5ZzHM")
        ]
    ]
)

sub_channel = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подписаться", url="https://t.me/fsoky_community")
        ]
    ]
)
