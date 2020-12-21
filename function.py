# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)


# def data(name,lastName,birthday,viloyat,email="shohzod@gmail.com",tel="+998938247501"):
#     """malumot toplaydi"""
#     user = {
#         "name":name,
#         "lastName":lastName,
#         "birthday":birthday,
#         "viloyat":viloyat,
#         "email":email,
#         "tel":tel
#     }

#     return user

# user=data("shohzod","Abdusamatov",2000,"jizzax","Sardor@gmail.com")
# print(user)



# 2-MASALA

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# def data(name,lastName,birthday,viloyat,email="shohzod@gmail.com",tel="+998938247501"):
#     """malumot toplaydi"""
#     user = {
#         "name":name,
#         "lastName":lastName,
#         "birthday":birthday,
#         "viloyat":viloyat,
#         "email":email,
#         "tel":tel
#     }
#     return user


# mijozlar=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting\n", end='')
#     name = input("Name: ")
#     lastName = input("lastName: ")
#     birthday = input("birthday: ")
#     viloyat = input("viloyat: ")
#     email = input(" email: ")
#     tel = input("tel: ")

#     mijozlar.append(data(name,lastName,birthday,viloyat,email,tel))
#     savol=input("yana malumot kiritaszmi? (ha/yo'q)")

#     if savol=='ha':
#         continue
#     else:
#         break
# print(mijozlar)


#   3-masalan

# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

# def max_aniqla(a,b,c):
#     """maxsimal qiymatni qaytar"""
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     elif c>=b and c>=a:
#         return c

# a,b,c=map(int,input(" uchta Sonlarni kiritng? \n>>> ").split())

# MAX=max_aniqla(a,b,c)
# print(MAX)


# 4-masala

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

# aylana={}

# radius=int(input("Aylanani Radiusini kiritng?\n>>>"))
# PI=3.14159
# def aylana_malumoti(radius):
#     aylana={
#         "Radius: ":radius,
#         "diametr: ":2*radius,
#         "peremetre:":2*PI*radius,
#         "yuzi:":PI*pow(radius,2)
#     }

#     return aylana

# aylana_1=aylana_malumoti(radius)
# print(aylana_1)

# 5-masala

# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
#11      2,3,5,7,11

# son=int(input("Sonni kiriting? >> "))
# tubsonlar=[]
# def tubSonni_qaytar(son):
#     for i in range(2, son):
#         ishora=True
#         for j in range(2, i):
#             if i%j==0:
#                 ishora=False

#         if ishora==True:
#             tubsonlar.append(i)

# tubSonni_qaytar(son)
# print(tubsonlar)


# 6-masala
# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

def Fibonachchi(son):
    """fiboanci sonlarni top"""
    sonlar=[1,1]
    for i in range(2,son):
        sonlar.append(sonlar[i - 1] + sonlar[i - 2])
        if sonlar[i]<son:
            continue
        else:
            break
    print(sonlar)


son =int(input("Son kiriting? >> "))
Fibonachchi(son)
