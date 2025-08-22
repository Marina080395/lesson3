
from address import Address
from mailing import Mailing

to_address = Address(index="123456", city="Москва", street="Ленинский проспект", house="10", apartment="5")

from_address = Address(index="654321", city="Санкт-Петербург", street="Невская набережная", house="20", apartment="15")

mailing = Mailing(to_address=to_address, from_address=from_address, cost=500, track="TRK123456789")

output_string = f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house}-{mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house}-{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."

print(output_string)
