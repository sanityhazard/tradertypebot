import asyncio
import random
import uuid

from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineQueryResultArticle, InputTextMessageContent


async def main():
    bot = Bot(token="6894515171:AAFVH-xO3DUBwMsFQBCxKbwsqn8mckmmxRo")
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


router = Router()


@router.inline_query()
async def inline_link(inline_query: types.InlineQuery) -> None:
    result_id: str = str(uuid.uuid4())
    random_number = random.randint(1, 100)
    numbers_dict = {
        range(1, 10): f'Сегодня я осторожный, поставлю {random_number}%',
        range(10, 30): f'Ебать я смелый, поставлю {random_number}%',
        range(30, 50): f'Я долбоеб, ставлю {random_number}%',
        range(50, 70): f'Я ЛУДИК ПИЗДЕЦ, ПОСТАВЛЮ {random_number}%',
        range(70, 90): f'Сегодня я готов проебать весь депозит, поставлю {random_number}%',
        range(90, 100): f'Я Олег. Ставлю {random_number}% с 100 плечом',
    }

    for key in numbers_dict:
        if random_number in key:
            message_text = numbers_dict[key]
            break

    item = InlineQueryResultArticle(
        input_message_content=InputTextMessageContent(message_text=message_text,
                                                      parse_mode='html'),
        title='Сколько % депа?',
        description='Узнайте сколько % депа вам надо поставить на следующую сделку',
        thumb_url='https://bullsonwallstreet.com/wp-content/uploads/2018/01/cryptocurrency-copy.png',
        id=result_id,
    )

    await inline_query.bot.answer_inline_query(results=[item],
                                               inline_query_id=inline_query.id,
                                               cache_time=1)


if __name__ == "__main__":
    asyncio.run(main())
