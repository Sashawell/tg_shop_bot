from aiogram.utils.formatting import Bold, as_list, as_marked_section


categories = ['Nike', 'adidas', 'New Balance', 'Puma', 'Vans']

description_for_info_pages = {
    "main": "Добро пожаловать!",
    "about": "Интернет магазин Nami, работаем круглосучно",
    "payment": as_marked_section(
        Bold("Варианты оплаты:"),
        "Картой в боте",
        "СПБ",
        "Крипта",
        marker="✅ ",
    ).as_html(),
    "shipping": as_list(
        as_marked_section(
            Bold("Варианты доставки/заказа:"),
            "Cdek",
            "Самовынос (сейчас прибегу заберу)",
            "Авито доставка",
            marker="✅ ",
        ),
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Категории:',
    'cart': 'В корзине пока что ничего нет :()'
}
