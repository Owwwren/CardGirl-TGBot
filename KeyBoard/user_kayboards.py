from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

def kb_start():
    builder = ReplyKeyboardBuilder()
    builder.button(text='Конкурс рефералов')
    builder.button(text='@OnlyFans')
    builder.button(text='@CardGirl')
    builder.button(text='О проекте')
    builder.adjust(1, 1, 1, 1)
    return builder.as_markup()



class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int

def inlinekb_start():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Рефералы",
        callback_data=MyCallback(foo="referals", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.button(
        text="@OnlyFans",
        callback_data=MyCallback(foo="onlyfans", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.button(
        text="@CardGirl",
        callback_data=MyCallback(foo="cardgirl", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.button(
        text="О проекте",
        callback_data=MyCallback(foo="abaut_project", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.adjust(1, 1, 1, 1)
    return builder.as_markup()

def inlinekb_ref():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="ТОП 10",
        callback_data=MyCallback(foo="10", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
#    builder.button(
#        text="ВСЕ",
#        callback_data=MyCallback(foo="all", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
#    )
    builder.button(
        text="Назад",
        callback_data=MyCallback(foo="back", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.adjust(1, 1)
    return builder.as_markup()




def inline_back():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Назад",
        callback_data=MyCallback(foo="back", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    return builder.as_markup()
def inline_backOnlyFans():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="OnlyFans NFT",
        url='https://getgems.io/girls-game'
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.button(
        text="Назад",
        callback_data=MyCallback(foo="back", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.adjust(1, 1)
    return builder.as_markup()
def inline_backCardGirl():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="CardGirl NFT",
        url='https://nft-bot.herokuapp.com/cardgirl',
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.button(
        text="Назад",
        callback_data=MyCallback(foo="back", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.adjust(1, 1)
    return builder.as_markup()
def inlinekb_back_ref():
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Назад",
        callback_data=MyCallback(foo="referals", bar="42")
        # Value can be not packed to string inplace, because builder knows what to do with callback instance
    )
    builder.adjust(1)
    return builder.as_markup()


