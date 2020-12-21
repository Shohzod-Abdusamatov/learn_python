# dostlar ={}

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1 # dostlarni sanash uchun o'zgaruvchi
# ishora=True
# while ishora:
#     savol="dostingizni ismini kiritng:"
#     ism=input(savol)
#     age=int(input(f"{ism.title()} ni yoshini kiriting? >>"))
#     dostlar[ism]=age
#     javob =input("Yana kiritasizmi: (ha/yo'q): ")
#     if javob=="ha":
#         ishora=True
#     else:
#         ishora=False

# for ism,age in dostlar.items():
#     print(ism+f"- {dostlar[ism]} yoshda")

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# Del_car='nexia'
# while Del_car in cars: # toki nexia cars ro'yxati ichida ekan...
#     cars.remove(Del_car) # nexia ni ro'yxatdan olib tashla
# print(cars)

# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho
# print(talabalar)

# AMALIYOT

# vazifa 1
# buyurtmalar =[]
# while True:
#     buyurtma=input("Nima buyurma qilmoqchisiz?>>")
#     buyurtmalar.append(buyurtma)
#     javob=input("Yana buyurtma bermoqchisiz? (ha/yo'q)")
#     if javob=="ha":
#         continue
#     else :
#         break
# print("sizning buyurtmalaringiz: ",buyurtmalar)

# vazifa 2
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

# e_bozor={}

# while True:
#     bozorlik=input("Nima olmoqchisiz? >> ")
#     narh=int(input("Narhi qancha ekan? > > "))
#     e_bozor[bozorlik]=narh
#     javob=input("yana narsa olaszmi ? (ha/yo'q)")

#     if javob=="ha":
#         continue
#     else :
#         break

# print(e_bozor)       
# 


# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

mahsulotlar={'olma':5000,'nok':1200,'anjir':2450,'non':500,'pomidor':4000}
ishora=True
count=0
while ishora:
    mahsulot=input("nima olmoqcisiz? >>")
    if mahsulot in mahsulotlar.keys():
        print(mahsulot," narhi ",mahsulotlar[mahsulot])
        count=count+mahsulotlar[mahsulot]
        javob=input(" yana narsa olaszmi? (ha/yo'q)")
        if javob=="ha":
            ishora=True
        else :
            ishora=False  
    else :
        print("bunday mahsulot yo'q")
        javob=input(" yana narsa olaszmi? (ha/yo'q)")
        if javob=="ha":
            ishora=True
        else :
            ishora=False 

print(count," so'm tolaysiz kassaga")        