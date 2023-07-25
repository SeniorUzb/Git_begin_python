#3ta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

#def max_number(number1, number2, number3):
#    max_num = number1
#    if max_num < number2:
#        max_num = number2
#    if max_num < number3:
#        max_num = number3
#    return max_num
#
#print(max_number(50, 100, 60))
    

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, 
#diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

def circle(radius, PI = 3.14):
    
    circle_info = {
        'radius' : radius,
        'diametr' : radius * 2,
        'perimetr' : 2* PI * radius,
        'yuza' : radius * PI**2
        }
    return circle_info

#radius = float(input("Enter radius: "))
#print(circle(radius))


# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta 
#  musbat sonlar)

def prime_number(fnumber, lnumber):
    prime_number_list = []
    if lnumber > fnumber:
        for n in range(fnumber, lnumber+1):
            count = 0
            for k in range(2, int(n/2)+1):
                if n % k == 0 and n > 1:
                    count+=1
            if count == 0 and n > 1:
                prime_number_list.append(n)
    return prime_number_list
#print(prime_number(-15, 22))

 # Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi 
 #ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  
 #Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng 
 #bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda 
 #boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13,
 #21, 34, 55,...
 
def fibonachi(number):
    fibonachi_list = []
    for n in range(0, number):
        if fibonachi_list == [] :
            fibonachi_list.append(1)
        elif len(fibonachi_list) == 1:
            fibonachi_list.append(fibonachi_list[0])
        else:
            fibonachi_list.append(fibonachi_list[n-1]+fibonachi_list[n-2])
    return fibonachi_list
print(fibonachi(100))
 
 

                    
            
            
            
            
            
        

