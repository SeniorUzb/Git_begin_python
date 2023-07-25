#Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili 
#va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing.
# Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy 
# qiling (masalan, tel.raqam, el.manzil)


def user_info(fname, lname, wborn, t_joy, email = None, number = ''):
    
    user_info_dict = {}
    user_info_dict['fname'] = fname
    user_info_dict['lname'] = lname
    user_info_dict['wborn'] = wborn
    user_info_dict['t_joy'] = t_joy
    user_info_dict['email'] = email
    if number != '':
        number = int(number)
    number = '+998 '+str(number)
    user_info_dict['number'] = number
    
    return user_info_dict
users_info = []
while True:
    fname = input("Enter your first name: ")
    lname = input("Enter your last  name: ")
    wborn = int(input("Enter your was born year: "))
    t_joy = input("Enter your was born place: ")
    email = input("Enter your email (ixtiyoriy): ")
    number = input("Enter your number (ixtiyoriy): ")
    users_info.append(user_info(fname, lname, wborn, t_joy, email, number))
    print()
    answer = input("Yana foydalanuvchi qo'shasizmi: (yes/no)  ")
    print()
    if answer == 'no':
        break
print(users_info)  
