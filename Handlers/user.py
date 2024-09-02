from aiogram.filters.callback_data import CallbackData
from pythonProject.Config import status, dp
from aiogram import types, Dispatcher, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from pythonProject.KeyBoard.user_kayboards import inlinekb_start, inlinekb_ref, inline_back, inlinekb_back_ref, inline_backOnlyFans, inline_backCardGirl
from pythonProject.dbconfig import SQLighter
from pythonProject.TOKEN import BOT_NAME, TOKEN
db = SQLighter('db.db')

bot = Bot(token=TOKEN)


##############InlineKeyboardMarkup####################
class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int
##############ДОП КОД####################
def get_top_referrar():
    users = db.get_all_refusers('all')
    table = db.get_all_refusers('referrars')
    #print(users)
    #print(table)
    lst = []
    for referrer in table:
        var = (f'{db.count_user(referrer[0])} {referrer[0]}')
        lst.append(var)
    lst_new = list(set(lst))
    revers = lst_new.sort(reverse=True)
    #print(lst_new)
    return lst_new
def set_top_referrar():
    msg = ''
    count = 10
    id = 0
    for user in get_top_referrar():
        id += 1
        if id <= count:
            first_name = str(db.get_firstname(user[2:])).replace(',', '').replace('(', '').replace(')', '').replace("'", '')
            print(first_name)
            referal_cout = user[0]
            msg += f'{id}. {first_name} - {referal_cout}\n'
        else:
            break
    return msg

##############ОСНОВНОЙ КОД####################
async def start(message: Message):
    global mes
    if not db.user_exist(message.from_user.id):
        print('true')
        start_command = message.text
        refferer_id = str(start_command[7:])
        if str(refferer_id) != "":
            if str(refferer_id) != str(message.from_user.id):
                db.add_user(id_user=message.from_user.id, id_ref=refferer_id, first_name=message.from_user.first_name)
                try:
                    mes = await bot.send_message(refferer_id, f'Новый реферал: {message.from_user.first_name}')
                except:
                    pass
            else:
                mes = await message.answer("По своей реферальной ссылки регистрироваться нельзя")
        else:
            db.add_user(id_user=message.from_user.id, first_name=message.from_user.first_name)
    print('false')
    mes = await message.answer_photo(
        photo='AgACAgIAAxkBAANNZikgHG8ouzyKN_WhfZbd0nA4EZYAArjeMRsWUklJaPfwF_jejBQBAAMCAAN5AAM0BA',
        caption="Привет друг! Мы рады что ты здесь😀\n", reply_markup=inlinekb_start())


async def start_callback(query: CallbackQuery, callback_data: MyCallback):
    global mes
    await mes.delete()
    mes = await query.message.answer_photo(photo='AgACAgIAAxkBAANNZikgHG8ouzyKN_WhfZbd0nA4EZYAArjeMRsWUklJaPfwF_jejBQBAAMCAAN5AAM0BA',
                               caption="Привет друг! Мы рады что ты здесь😀\n",
                               reply_markup=inlinekb_start())

async def callback_referal_menu(query: CallbackQuery, callback_data: MyCallback):
    global mes
    await mes.delete()
    mes = await query.message.answer_photo(photo="AgACAgIAAxkBAANTZikgKb5fqnnqh5MwFc5B1ItHfAwAAtDeMRsWUklJVh6hlzWh7FEBAAMCAAN4AAM0BA",
                               caption='ТОП 10 пользователей, пригласивших наибольшее количество друзей, получат ценные призы от Фаундеров Telegram Game CardGirls.\n'
                                       'Твоя реферальная ссылка:\n'
                                       f'https://t.me/{BOT_NAME}?start={query.from_user.id}\n'
                                       f'Кол-во рефералов: {db.count_user(query.from_user.id)}', reply_markup=inlinekb_ref())


async def callback_10ref(query: CallbackQuery, callback_data: MyCallback):
    top_referrar_users = set_top_referrar()
    global mes
    await mes.delete()
    mes = await query.message.answer_photo(photo="AgACAgIAAxkBAANTZikgKb5fqnnqh5MwFc5B1ItHfAwAAtDeMRsWUklJVh6hlzWh7FEBAAMCAAN4AAM0BA",
                               caption='ТОП 10 рефоводов:\n'
                               f'{top_referrar_users}', reply_markup=inlinekb_back_ref())
#async def callback_allref(query: CallbackQuery, callback_data: MyCallback):
#    await query.answer('работает')
#    await query.message.answer('Список рефералов')


async def callback_OnlyFans(query: CallbackQuery, callback_data: MyCallback):
    global mes
    await mes.delete()
    mes = await query.message.answer_photo(photo="AgACAgIAAxkBAANPZikgICPDDxnYvTgx01z9xpKwrIEAAs7eMRsWUklJfOCQ_iwcT1YBAAMCAAN5AAM0BA",
                               caption='The girls admire the beautiful view.'
                                       'Well, when this view is as naked as'
                                       'possible, how can you resist the'
                                       'temptation to admire? Each new card is'
                                       'distinguished byy the uniqueness of'
                                       'women who like to stand out for their'
                                       'elegance, endurance and personality.', reply_markup=inline_backOnlyFans())
async def callback_CardGirl(query: CallbackQuery, callback_data: MyCallback):
    global mes
    await mes.delete()
    mes = await query.message.answer_photo(photo="AgACAgIAAxkBAANRZikgJWkrbrtaMWz6T0nt7ImvrJIAAs_eMRsWUklJtAYPoIS9s-8BAAMCAAN5AAM0BA",
                               caption='Female beauty has been appreciated since'
                                       'prehistoric times. The presented cards'
                                       'cover a variety of styles. Some show'
                                       'mastery in depicting female sensuality,'
                                       'others lack subtlety and deeper meaning.'
                                       'We suggest that you judge for'
                                       'yourself.Stylish playing cards with the'
                                       'image of glamorous girls from the world'
                                       'of alternative reality.', reply_markup=inline_backCardGirl())
async def callback_about_the_project(query: CallbackQuery, callback_data: MyCallback):
    global mes
    await mes.delete()
    mes = await query.message.answer_photo(photo="AgACAgIAAxkBAANNZikgHG8ouzyKN_WhfZbd0nA4EZYAArjeMRsWUklJaPfwF_jejBQBAAMCAAN5AAM0BA",
                               caption='Telegram Game CardGirls — NFT-игра, это'
                                       'место, где приоткрываются врата в'
                                       'виртуальный мир знакомств, она сочетает в'
                                       'себе развлекательную и экономическую'
                                       'сторону, позволяет получать'
                                       'дополнительный доход, реализовывать свой'
                                       'творческий потенциал и монетизировать его.'
                                       'CardGirls –  онлайн-игра, которая использует'
                                       'невзаимозаменяемые токены (NFT) в'
                                       'качестве игровых активов. Особенность NFT'
                                       'в том, что они используют технологию'
                                       'блокчейн TON для подтверждения'
                                       'уникальности.'
                                       'Коллекция NFT CardGirls: getgems.io/girls-game'
                                       'General chat: @GirlsCard_ton', reply_markup=inline_back())

def register_handler_user(dp: Dispatcher):
    dp.message.register(start, Command(commands= ['start']))
    dp.callback_query.register(callback_OnlyFans, MyCallback.filter(F.foo == 'onlyfans'))
    dp.callback_query.register(callback_CardGirl, MyCallback.filter(F.foo == 'cardgirl'))
    dp.callback_query.register(callback_about_the_project, MyCallback.filter(F.foo == 'abaut_project'))
    dp.callback_query.register(callback_referal_menu, MyCallback.filter(F.foo == 'referals'))
    dp.callback_query.register(callback_10ref, MyCallback.filter(F.foo == '10'))
    #dp.callback_query.register(callback_allref, MyCallback.filter(F.foo == 'all'))
    dp.callback_query.register(start_callback, MyCallback.filter(F.foo == 'back'))