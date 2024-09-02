from aiogram import Dispatcher
from aiogram.filters.state import StatesGroup, State

class status(StatesGroup):
    start = State()

dp = Dispatcher()