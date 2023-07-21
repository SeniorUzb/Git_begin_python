#dars-8

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

states = ["Uzbekistan", "Kazakhistan", "Tadjikistan", "Kyrgizistan", "Afganistan"]

# Ro'yxatning uzunligini konsolga chiqaring

print(len(states))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

print(sorted(states))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

print(sorted(states, reverse=True))

# Asl ro'yxatni qaytadan konsolga chiqaring

print(states)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring

states.reverse()
print(states)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

states.sort()

print(states)

states.sort(reverse=True)

print(states)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

numbers = list(range(120, 1201, 2))

print(numbers)

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

numbers_sum = sum(numbers)

print(numbers_sum)

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

max_number = max(numbers)

min_number = min(numbers)

print("min =", min_number, "   max =", max_number)

# Ro'yxatdagi elementlar sonini hisoblang

numbers_list_len = len(numbers)

print(numbers_list_len)

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

numbers_begin = numbers[:20]

numbers_middle = numbers[int(numbers_list_len/2)-10: int(numbers_list_len/2)+10]

numbers_end = numbers[numbers_list_len-20:]

print(numbers_begin)
print(numbers_middle)
print(numbers_end)

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting

eats = ["osh", "manti", "lag'mon", "sho'rva", "kabob"]

# nonushta degan yangi ro'yxatga taomlardan nusxa oling

breakfasts = eats[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

breakfasts.remove("osh")
breakfasts.remove("kabob")
breakfasts.append("cake")
breakfasts.append("sugar")
breakfasts.insert(3, "honey")

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

print(eats)
del breakfasts("sho'rva")
print(breakfasts)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.

breakfasts = tuple(breakfasts)

print(breakfasts)

breakfasts[0] = "milk"







