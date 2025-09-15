


#07-dars LIST

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# mevalar = ['olma','nok', 'banan', 'qulupnoy']
# narhlar = [5500, 7000, 14000, 2500]

# sonlar = ['bir', 'ikki', 3, 4, 5]
# ismlar = []


# qushlar = ['burgut', 'lochin', 'qarg\'a', 'ukki', 'lochin']

# bozorlik = ['guruch', 'piyoz', 'un', 'sut', 'gosht']

# mahsulot = bozorlik.pop(1)

# print("Men ", mahsulot, "sotib oldim.")
# print("Oliinmagan mahsulotlar: ", bozorlik)
 
# ismlar = ['zarif', 'abbos', 'firdavs', 'aziz']

# print("Salom ", ismlar[1].title(), "bugun choyxona bo'ladimi ?")
# print(ismlar[2].title(), "choyxonaga borasanmi")

# sonlar = [34, 42,54.98, -22, 4.6, 21]

# sonlar[1] + 12
# sonlar[5]-23
# sonlar[-1]/7
# sonlar[4] = 3.14159*12

# print(sonlar)

# t_shaxslar = ['molik', 'noman', 'shafeiy', 'ahmad']

# z_shaxslar = ['zufar', 'abdulloh', 'sodiq', 'yusuf']

# salaf = t_shaxslar.pop()
# xolaf = z_shaxslar.pop(0)

# print("Men tarixiy shaxslardan", salaf, "bilan, zamonaviy shaxslardan", xolaf, "bilan ko'rishishni hohlardim")

# son = int(input("Bir nechta raqamlar kiriting: "))

# dostlar = ['ali', 'vali', 'gani', 'usmon', 'rovshan']
# dostlar.sort(reverse=True)

# print(dostlar)

# cars = ['bmw', 'ford', 'dodge', 'toyota', 'porsche']

# cars.sort()

# cars = ['bmw', 'ford', 'dodge', 'toyota', 'porsche']

# cars.sort(reverse=True)


# cars = ['bmw', 'ford', 'Dodge', 'toyota', 'porsche']
# cars.sort()
# # avto = sorted(cars)

# print("Cars >a>z> >", cars)
# print("cars bardak >", avto)



# raqamlar = list(range(1, 22))

# raqamlar.sort(reverse = True)

# # 
# cars = ['bmw', 'ford', 'Dodge', 'lacetti', 'toyota', 'porsche', 'tesla']

# narhlar = [12000, 32600, 45990, 9800, 7500, 2250, 3750]

# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)

# print("Eng arzoni: ", arzon, "Eng qimmati: ", qimmat, "Umumiy: " , jami)


# qushlar = ['burgut', 'lochin', "qarg'a", 'ukki', 'lochin', 'chumchuq']

# toys = ('bus', 'car', 'bear', 'lion', 'bear', 'monkey', 'car', 'bear')

# print(toys.count('bear'))
# print(toys.count('car'))
# print(toys.count('puma'))

# hayvonlar = ("sher", "yo'lbars", "bo'ri", "qoplon", "timsoh", "shoqol")
# print(hayvonlar.index("sher"))
# print(hayvonlar.index("bo'ri"))
# print(hayvonlar.index("shoqol"))

# matn = "Programming"

# matn[:5]

# matn[3:8] 

# matn[-4:] 

# matn[::2] 

# matn[::-1]

# countries = ['turkey', 'qatar', 'switzerland', 'misr', 'andalus', 'kipr', 'iran']


# print(countries)

# nomerlar = list(range(12,120,2))

# # print("umumiy", nomerlar)
# # print("Eng kichigi", min(nomerlar))
# # print("Eng kattasi", max(nomerlar))
# # print("jami", sum(nomerlar))

# # a = min(nomerlar)
# # b = max(nomerlar)

# # print("3510-12=",b-a)

# print("Avalgi 5ta raqam", nomerlar[:5])
# print("Oxirgi 5ta raqam", nomerlar[-6:])
# print("O'rtadagi raqamlar", nomerlar[45:65])

# taomlar = ['osh', 'shashlik', 'somsa', 'norin', 'moshxorda', "sho'rva", "menemen"]

# nonushta = taomlar[:]

# nonushta.remove('osh')
# nonushta.remove('somsa')
# nonushta.remove('moshxorda')
# nonushta.remove("sho'rva")

# nonushta.append("qaymoq")
# nonushta.insert(1, "bo'tqa")

# print("Tushlik uchun taomlar: ", taomlar)
# print("Nonushta uchun taomlar: ", nonushta)

# nonushta = tuple(nonushta)


# raqamlar_tuple = (20, 30, 40, 50, 60, 70)
# print(raqamlar_tuple[3])
# print(raqamlar_tuple.count(20))
# print(raqamlar_tuple.index(40))


# raqamlar_list = [10, 20, 30, 40, 50, 60]

# print(raqamlar_list.count(30))
# print(raqamlar_list.index(20))

# raqamlar_list.append(77)
# raqamlar_list.remove(30)
# raqamlar_list.pop(4)

# print(raqamlar_list)



# sonlar_tuple = (15, 25, 35, 45, 55, 65)
# sonlar_tuple = list(sonlar_tuple)

# sonlar_tuple.insert(2, 33)
# sonlar_tuple.remove(35)

# sonlar_tuple = tuple(sonlar_tuple)

# countries = ['korea', 'china', 'india', 'turkey', 'japan']

# print("Alifbo tartibida: ",sorted(countries))
# print("Alifboga teskari tartibda: ", sorted(countries, reverse=True))
# print(len(countries))
# print(countries)

# juft_s = list(range(12, 1201,2))

# print("jadval uzunligi:", len(juft_s))
# print("eng kichigi:", min(juft_s))
# print("eng kattasi: ", max(juft_s))
# print("ikkovini farqi: ", max(juft_s) - min(juft_s))
# print("yig'indisi: ", sum(juft_s))


# juft_s = list(range(12, 1201,2))

# orta = len(juft_s)//2
 

# print("Avvalgi 20ta son", juft_s[:20])
# print("O'rtadagi 20ta son", juft_s[orta-10:orta+10])
# print("Oxirgi 20ta son", juft_s[-20:])



# toq_s = list(range(12, 1201,2))

# mid = len(toq_s)//2
 

# print("Avvalgi 20ta son", toq_s[:20])
# print("O'rtadagi 20ta son", toq_s[mid-10:mid+10])
# print("Oxirgi 20ta son", toq_s[-20:])


# mehmonlar = ['Ali', 'Vali', "G'ani", "Anvar", "Ruslan"]
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-may kuni nahorga taklilf qilamiz")
#     print("Hurmat bilan Palonchiyevlr oilasi.")

# sonlar = list(range(1, 11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2},ga teng")
    
# sonlar = list(range(11))

# sonlarni_kvadrati = []
# for son in sonlar:
#     sonlarni_kvadrati.append(son**2)
    
# print(sonlar)
# print(sonlarni_kvadrati)

# dostlar = []
# print("5ta eng yaqin do'stingizni ismini kiriting: ")

# for dost in range(5):
#     dostlar.append(input(f"{dost+1}-do'stingizni kiriting: "))
    

# shaxslar = ('lenin', 'Stalin', 'Gitler', "Cherchil", 'mussalini')
# for shaxs in shaxslar:
#     print(f"Bu qonxor {shaxs}ni taniysizmi ?")
    
# print(F"Kod {len(shaxslar)} martta takrorlandi")

# toqmoq = list(range(1,101,2))
# for k in toqmoq:
#     print(f"{k} sonining kvadrati {k**2} ga teng")


# toqmoq = list(range(1,101,2))
# for k in toqmoq:
#     print(k**3)
# print(f"Jami {len(toqmoq)}ta toq son topildi")

    
    
# cinema = []  # bo'sh royxat
# print("5ta eng sevgan filmingizni ayting >>>") # oddiy matn halos
# for kino in range(5): # for sikli va range ro'yxat tuzayapti
#     cinema.append((input(f"{kino+1}-sevimli filmingizni kiritng >>>" )))
# # 
# print(cinema)


# royxat = []
# print("Bugun kimlar bilan ko'rishdingiz ?")
# for kishi in range(6):
#     royxat.append(input(f"siz bila suhbatlashgan {kishi+1}-kishi kim edi >"))
    
# print(f"Siz bugun suhbatlashgan kishilar > {royxat}")

# kantakt = ['fedya', 'zarif', 'abbos', 'aziz', 'turon', 'otash']
# for k in kantakt:
#     print(f"Salom {k.title()} bugun kechasi futbolga borasanmi ?")
# print("Xabar jami ", len(kantakt), "kishiga yuborildi")

# oyinlar = ['Fifa', 'world of tanks', 'csgo', 'pubg', 'minecraft']
# yulduzlar = [3, 4, 2, 1, 5]
# for oyin in range(len(oyinlar)):
#     yulduzcha = "*" * yulduzlar[oyin]
#     print(f"{oyinlar[oyin]}  -  {yulduzcha} yulduzchaga ega")
    
    
# U+2764

# Restoranlar = ['norin', 'osh', 'shashlik', "sho'rva", 'somsa']
# darajalar = [3, 4, 1, 5, 2]

# for r in range(len(Restoranlar)):
#     darra = "❤" * darajalar[r]
#     print(f"{Restoranlar[r]}  -  {darra}, ga teng")
           
# ..>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
           
# Restoranlar = ['norin', 'osh', 'shashlik', "sho'rva", 'somsa']
# darajalar = [3, 4, 1, 5, 2]

# for r in range(len(Restoranlar)):
#     darra = "❤" * darajalar[r]
#     print(f"{Restoranlar[r]}  -  {darra} ga teng")

   #❤

# kinolar = ['Interstellar', 'Inception', 'Matrix', 'Avatar', 'Titanic']
# darajalar = [4, 3, 5, 1, 2]

# for k in range(len(kinolar)):
#     daraja = '*' * darajalar[k]
#     print(f"{kinolar[k]} {daraja}darajaga ega ")
    
    
# mevalar = ['olma', 'anor', 'uzum', 'banan', 'shaftoli']
# for meva in mevalar:
#     print(meva.upper())

# futbolchilar = ['pele', 'maradona', 'messi', 'ronaldo', 'cruiyf']
# urevin = [4,1,2,5,3]
# for fut in range(len(futbolchilar)):
#     dar = '❤' * urevin[fut]
#     print(f"{futbolchilar[fut]} , ushbu {dar} darajada")
      
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# avtolar = ['audi', 'bmw', 'mercedes', 'porsche', 'ww']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else: 
#         print(avto.title())
        
    
# ism = "Ali"

# ism.lower() == "ali"

# ism = input('Ismingiz nima ?\n>>> ')
# if ism.lower() != 'ali':
#     print(f"Uzr {ism.title()} Biz Alini kutayapmiz")
# else:
#     print("Salam !  Ali")

# javob = float(input("12*6 nechiga teng ?  >>> "))
# if javob != 72:
#     print("Javobingiz xato")
    

# yosh = int(input("Yoshingiz nechida ? "))
# if yosh >= 18:
#     print("Xush kelibsiz !")
# else:
#     print('Kirish mumkin emas')
    

# login = input("Yangi login kiriting ! ")
# if len(login) <=8:
#     print("Login kamida 8 harfdan iborat bo'lishi kerak")
# else:
#     print("Yangi login tasdiqlandi !")
    
# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2025 - yil < 18:
#     print(f"Sizni yoshingiz {2025-yil}da ekan.\nSiz voyaga yetagansiz")
# else:
#     print("Xush kelibsiz")
    
# yosh = int(input('Yoshingiz nechida ? '))
# if yosh > 65: print("Siz nafaqadagi odamsiz !")

# x, y = 32, 22
# print("x>y") if x>y else print("x<y")


# cars = ['gm', 'lambo', 'ford', 'dodge', 'merc', 'bmw']
# for car in cars:
#     if car != "bmw":
#         print(car.title())
#     else:
#         print(car.upper())

# lopp = (input("Manzilingizni kiriting: "))
# if lopp.lower() != "barbarossa":
#     print("Uka bu yerdan sirpan")
# else:
#     print("Xush kelibsiz og'a")

# x = float(input("Birinchi raqamni kiriting: "))
# y = float(input("Ikkinchi raqamni kiriting: "))
# if x == y:
#     print("Siz kiritgan sonlar teng.")
# else:
#     print("Siz kiritgan sonlar teng emas")
    

# son = int(input("Istalgan soningizni kiriting: "))
# if son < 0:
#     print("bu manfiy son !")
# else:
#     print("Bu musbat son")

# son = int(input("Istalgan sonni kiriting: "))
# if son > 0:
#     ildiz = son ** 0.5
#     print(f"{son}ning ildizi {round(ildiz, 2)}ga teng")
# else:
#     print("Musbat son kiriting")
    


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    

    
# son = int(input("Istalgan sonni kiriting: "))
# if son > 0:
#     print("Bu musbat son")
# else:
#     print("Bu manfiy son")
    
# yosh = int(input("Yoshingiz nechchida: "))
# if yosh <= 6:
#     print("Sizga kirish bepul !")
# elif yosh <= 12:
#     print("Sizga kirish 5000 so'm ")
# elif yosh <= 17:
#     print("Sizga kirish 7000 so'm ")
# else:
#     print("Sizga kirish 10000 so'm ")
    

# yosh = int(input("Yoshingiz nechchida: "))
# if yosh <= 6:
#     narx = 'bepul'
# elif yosh <= 12:
#     narx = 5000
# elif yosh <= 17:
#     narx = 7000
# else:
#     narx = 10000
    
# print(f"Sizga kirish {narx} so'm")

# kun = input("Bugun qanday kun ? ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print("Bugun dam olish kuni !")
# else:
#     print("Bugun ish kuni !")
    
    
# kun = input("Bugun nima kun ? ")
# harorat = float(input("Havo harorati qanday ? "))

# if kun.lower() == "yakshanba" and harorat >= 31:
#     print("Kettik unda cho'milgani ")
# elif kun.lower() == 'yakshanba' and harorat <= 31:
#     print("Uyda dam olamiz Bro !")    
    
    
# kun = input("Bugun nima kun ? ")
# harorat = float(input("Havo harorati qanday ? "))

# if kun.lower() == "yakshanba" or kun.lower() == "shanba" and harorat >= 31:
#     print("Kettik unda cho'milgani ")
# elif kun.lower() == 'yakshanba' or kun.lower() == "shanba" and harorat <= 31:
#     print("Uyda dam olamiz Bro !")    
    
# narx = 15000
# choy = False
# salat = True
# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000

# print(f"Jami {narx} so'm bo'ldi ")

# narx = 15000
# choy = 1
# non = 0
# salat = 0
# assorti = 1
# qaymoq = 1

# if choy:
#     print('Mijoz choy sotib oldi')
#     narx = narx + 3000
# if non:
#     print('Mijoz non sotib oldi')
#     narx = narx + 5000
# if salat:
#     print('Mijoz salat sotib oldi')
#     narx = narx + 12000
# if assorti:
#     print('Mijoz assorti sotib oldi')
#     narx = narx + 25000
# if qaymoq:
#     print('Mijoz qaymoq sotib oldi')
#     narx = narx + 12000

# print(f"Jami {narx} so'm bo'ldi ")



# menu = ['osh', 'somsa', 'norin', 'xonim', 'manti', 'moshxorda']

# ovqat = input("Nima ovqat yeysiz ? ")
# if ovqat in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday taom yo'q")
    

# menu = ['osh', 'somsa', 'norin', 'xonim', 'manti', 'moshxorda']
# buyurtmalar = ['somsa', 'nok', "sho'rva", 'manti']
# for taom in buyurtmalar:
#     if taom in menu:
#         print("Buyurtma qabul qilindi !")
#     else:
#         print(f"Afsuski bizda {taom} yo'q")
        

# son = int(input("Juft son kiriting: "))
# if son == 0:
#     print("Bu na juft vana toq son emas !")
# elif son % 2 == 0:
#     print("Juft son tasdiqlandi. ")
# else:
#     print("Siz toq son kiritdingiz. ") 
    

# age = int(input("Yoshingizni kiriting: "))
# if age <= 4 or age >= 60:
#     print("Siz muzeyga bepul kirasiz !")
# elif age < 18:
#     print("Sizga muzeyga kirish 10.000 so'm.")
# else:
#     print("Sizga kirish 15.000 so'm")


# dukkan = ['banan', 'tvorog', 'flavis', 'esse', 'konfet', 'qaymoq', 'non', 'sok', 'kiwi']
# savatcha= []
# yoq_mahsulot = []
# for n in range(5):
#     mahsulot = input(f"{n+1}-mahsulotingizni kiriting: ")
#     if mahsulot in dukkan:
#         savatcha.append(mahsulot)
#         print(f"{mahsulot} savatchaga solindi")
#     else:
#         yoq_mahsulot.append(mahsulot)
#         print(f"{mahsulot} hozircha bizda mavjud emas")
        
# print(f"Bu sizning savatchangizdagi mahsulotlar \n{savatcha}")
# print(f"Bu bizda hozirch yo'q bo'lgan mahsulotlar \n{yoq_mahsulot}")
        
# users = ['anvar', 'John', "ibrohiym", 'solih433', 'Mikel']
# users = [user.lower() for user in users]

# login = input("Yangi login kiriting: ").lower()
# if login in users:    
#   print(f"Ushbu {login} username band ! \nBoshqa login tanlang")
# else:
#   print("Yangi login tasdiqlandi !")
  
  
# son = int(input("Istalgan sonni kiriting: "))
# for w in range(2,11):
#     if son % w == 0:
#         print(f"{son} soni {w} soniga qoldiqsiz bo'linadi ")
#     else:
#         print(f"{son} soni {w} soniga qoldiqli bo'linadi")

# son = int(input("Istalgan soningizni kiriting: "))
# if son % 2 == 0:
#     print(f"Ushbu {son} kiritgan soningiz  juft son")
# else:
#     print(f"Ushbu {son} kiritgan soningiz toq son")
        
# son = int(input("Istagan soningizni kiriting: "))
# if son % 2 != 0:
#     print(f"{son} toq son hisoblanadi") 
# else:
#     print(f"{son} juft sonlardan hisoblanadi")


# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# if x == y:
#     print(f"Bu {x} va {y} ikkita qiymat tengdur")
# elif x > y:
#     print(f"{x}>{y} Bu yerda {x} soni katta")
# elif x < y:
#     print(f"{x}<{y} Bu yerda {y} soni katta")
    

# ball = int(input("1 dan 100 gacha ball sistemada taxi xizmatini baholang !\n>>> "))
# if ball >= 90:
#     print("Super xizmat ko'rsatganimizdaan hursandmiz")
# elif ball >= 80:
#     print("Yaxshi hizmat ko'rsatganimizdan mamnunmiz")
# elif ball >= 70:
#     print("Bundanda yaxshi hizmat ko'rsatishga harakat qilamiz")
# elif ball >= 55:
#     print("Yaxshi hizmat ko'sata olmaganimizdan mahzumiz")
# else:
#     print("Biz taxi hodimi bilan tushuntirish ishlari olib boramiz")


MAX_TRIES = 3
correct_login = 'admin'
correct_pass = '123321'

tries = 0

while tries < MAX_TRIES:
    login = input("Loginni kiriting: ").strip().lower()
    parol = input("Parolni kiriting: ").strip()
    
    if login == correct_login and parol == correct_pass:
        print("Xush kelibsiz Admin amaki")
        break
    else:
        tries +=1
        qolgan = MAX_TRIES - tries
        if qolgan > 0:
            print(f"Login yoki parol xato. Sizda {qolgan} urinish qoldi")
        else:
            print("Uka bu yerdan yuqolib qol !\nHozir admin kelib qoladi")
    
      
x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
z = int(input("Uchinchi sonni kiriting: "))

if x + y > z or x + z > y or z + y > x:
    print("Uchburchak yasay olamiz")
else:
    print("Bu o'lchamlardan uchburchak yasab bo'lmaydi")
    
x = int(input("Birinchi sonni kiriting: "))
y = int(input("Ikkinchi sonni kiriting: "))
z = int(input("Uchinchi sonni kiriting: "))

if x + y > z and x + z > y and y + z > x:
    print("✅ Uchburchak yasash mumkin!")

    if x == y == z:
        print("👉 Bu uchburchak teng tomonli")
    elif x == y or x == z or y == z:
        print("👉 Bu uchburchak teng yonli")
    else:
        print("👉 Bu uchburchak turli tomonli")
else:
    print("❌ Bu o'lchamlardan uchburchak yasab bo'lmaydi")


son = int(input("Istagan soningizni kiriting: "))
if son > 0:
    print("Bu son musbat")
elif son < 0:
    print("Bu son manfiy")
else:
    print("Bu son na manfiy vana musbat")
    

yosh = int(input("Yoshingizni kiriting: "))
if yosh < 7:
    print("Siz maktabga chiqmagansiz")
elif yosh <= 18:
    print("Siz maktabda o'qiysiz.")
elif yosh <=25:
    print("Siz ehtimol universitetda o'qiysiz yoki ishlaysiz")
else:
    print("Umrizni yarmini yashab qo'yibsiz")
    
son = int(input("Istalgan soningizni kiriting: "))
if son % 3 == 0 and son % 5 ==0:
    print("Fizzbuzz")
elif son % 3 == 0:
    print("Fizz")
elif son % 5 == 0:
    print("Buzz")
else:
    print(son)
      

son = int(input("Istalgan soningizni kiriting: "))
if son > 0:
    yigindi = sum(range(1, son+1,))
    print(f"{son}ning yig'indisi {yigindi}ga teng")
elif son < 0:
    print("Manfiy son kiritdingiz")
else:
    print("0 bu raqam emas")

numbers = []
musbat_toq = []
musbat_juft = []


for raq in range(5):
    kraqam = int(input(f"{raq+1}-raqamni kiriting: "))
    
    if kraqam > 0 and kraqam % 2 == 0:
        musbat_juft.append(kraqam)
    elif kraqam > 0 and kraqam % 2 != 0:
        musbat_toq.append(kraqam)
    else:
          print("Musbat son kiriting !")
#______________________________________________________________________

yigindi_m_j = sum(musbat_juft)
print(f"Siz kiritgan juft sonlarning yig'indisi {yigindi_m_j}ga teng")
yigindi_m_t = sum(musbat_toq)
print(f"Siz kiritgan toq sonlarning yig'indisi {yigindi_m_t}ga teng")

son = int(input("Istalgan musbat soningizni kiriting: "))
if son > 0:
    print(f"Quyida siz kiritgan {son} sonini karra jadvali")
    for ka in range(1,11):
        print(f"{son} * {ka} = {son * ka}")
else:
        print("Faqat musbat son kiriting")
        

x = int(input("Birinchi soningizni kiriting: "))     
y = int(input("Ikkinchi soningizni kiriting: "))
z = int(input("Uchinchi soningizni kiriting: "))

if x >= y and x >= z:
    print(f"{x} soni siz kiritgan sonlarni ichida eng kattasidur.")
elif y >= x and y >= z:
    print(f"{y} soni siz kiritgan sonlarni ichida eng kattasidur.")
elif z >= y and z >= x:
    print(f"{z} soni siz kiritgan sonlarni ichida eng kattasidur.")

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>







               


















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

        
    
        

    
    


























