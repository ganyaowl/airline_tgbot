from aiogram.types import LabeledPrice

TOKEN = "Your token"

PAYMENT_TOKEN = "Payment token"
ECONOMY_PRICE = LabeledPrice(label="Оплата за билет", amount=499_900*100) # считает в копейках, поэтому умножаем на 100
BUSINESS_PRICE = LabeledPrice(label="Оплата за билет", amount=999_900*100)

TECH_SUPPORT = "https://t.me/Cayatceek2006"

locations = ["Ташкент", "Самарканд", "Бухара", "Нукус"]
tariffs = ["Эконом", "Бизнес"]
prices = {"Эконом": 499_900, "Бизнес": 999_900}
