countries = {"Россия": "Москва",
            "Германия": "Берлин",
            "Италия": "Рим"}
print("a) Пары ключ-значение: ")
for country, capital in countries.items():
    print(country,"-", capital)
country_b = "Россия"
print("\nb) Столица для страны", country_b, ":", countries.get(country_b, "Страна не найдена"))
sort = sorted(countries.keys())
print("\nc) Произведена сортировка в алфавитном порядке:")
for country in sort:
    print(country, "-", countries[country])