from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboards():
    menu = ReplyKeyboardMarkup(
        [
            [
                KeyboardButton(text='Menyu🍴')
            ],
            [
                KeyboardButton(text='Mening buyurtmalarim🗒️')
            ],
            [
                KeyboardButton(text='Savat📥'),
                KeyboardButton(text='Aloqa📞')
            ],
            [
                KeyboardButton(text='Xabar Yuborish🗳'),
                KeyboardButton(text='Sozlamalar⚙️')
            ],
            [
                KeyboardButton(text='Biz haqimizda🔤')
            ]
        ],
        resize_keyboard=True
    )

    return menu