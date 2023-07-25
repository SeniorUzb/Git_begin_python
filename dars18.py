# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

''' 

print("Mijoz sahifasi")

buyurtmalar = []

flag = True
n = 1
print("Chiqish 'exit'")
while flag:
    buyurtma = input(f"{n} - buyurtmangizni kiriting: ")
    n+=1
    if buyurtma != "exit":
        buyurtmalar.append(buyurtma)
        question = input("Yana buyurtma berasizmi? (ha/yoq) : ")
        if question == "yoq":
            flag = False
    else:
        flag = False
print()
print("Sizning buyurtmalaringiz!")
for buy in buyurtmalar:
    print(buy.title())
    '''
 
    
 
''' e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi 
dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar 
(mahsulot va uning narhi) kiritishni so'rang. '''

'''
e_bazar = {}

flag = True
n = 1
print("Chiqish ('exit')")
while flag:
    buyurtma = input(f"{n} - mahsulotni kiriting: ")
    n+=1
    if buyurtma != 'exit':
        narx = int(input(f"{buyurtma}ning narxini kiriting: "))
        e_bazar[buyurtma] = narx
    else:
        flag = False
    
    
print(e_bazar)    '''




'''
Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi 
har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
(tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa 
 mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni
 kor'sating.  '''
 
 
print("E-Bazarga xush kelibsiz!")

flag1 = True

e_bazar_mah = {}

xaridlar = {}

hisob = 0

while flag1:
    print("Admin (1) Xaridor (2) Chiqish (ixtiyoriy key)")
    kirish = input("Bo'limni tanlang : ")
    flag2 = True
    flag3 = True
 #'''   if int(kirish) != 1:
  #      flag1 = False   '''
        
    if kirish == "1":
        print("Admin paneli!")
        while flag2:
            print("Bo'limdan chiqish 'exit' ")
            mahsulot = input("Mahsulot kiriting: ")
            if mahsulot.lower() != "exit":
                narx = input(f"{mahsulot}ning narxini kiriting: ")
                e_bazar_mah[mahsulot] = int(narx)
            else:
                flag2 = False
    elif kirish == "2":
        print("Xaridor paneli!")
        while flag3:
            print("Menyu (1), Xarid qilish (2), Xaridlar (3), Chiqish(ixtiyoriy key)")
            menu = input("Bo'limni tanlang: ")
            if menu == '1':
                for e_mah, e_narx in e_bazar_mah.items():
                    print(f"{e_mah} : {e_narx}")
                
            elif menu == '2':
                flag5 = True
                print("Xaridlar menyusidan chiqish (exit)")
                while flag5:
                    xarid = input("Xarid qilmoqchi bo'lgan mahsulotni kiriting: ")
                    if xarid == 'exit':
                        flag5 = False
                    elif xarid in e_bazar_mah:
                        xaridlar[xarid] = e_bazar_mah[xarid]
                        hisob+=e_bazar_mah[xarid]
                        del e_bazar_mah[xarid]
                    else:
                        print("Afsuski bu mahsulot bizda yoq!")
                        print()
            elif menu == '3':
                if xaridlar == {}:
                    print("Savatchangiz bo'sh!")
                    continue
                else:
                    print("Xaridlaringiz!")
                    for xarid0 in xaridlar:
                        print(xarid0, " : ",xaridlar[xarid0])
                    print("Hisob: ",hisob)
                    print("Xaridngiz uchun rahmat!")
            else:
                flag3 = False
    
    
    else:
        flag1 = False
