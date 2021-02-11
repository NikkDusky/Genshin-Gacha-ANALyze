import random
import os

os.system("cls") #Clear terminal
os.system("title Genshin Gacha ANALyze") #Name for terminal

tenPullStr = "" #just a variables
x = 0
violet_pulls = 0
legendary_pulls = 0

total_violet = 0    #variables for the number of *4 *5 *3 items (weapons or characters)
total_legendary = 0
total_blue = 0

chance_on_legendary = "0.6" #just a official chances to get items in one pull of gacha shit
chance_on_violet = "5.1"
chance_on_blue = "94.3"

def hero_or_gun():
    herogun = random.choices(['Герой', 'Оружие'], weights=[50, 50]) #50/50 simple func, weapon or character we get.
    return herogun

def one_pull():

    global violet_pulls    #take global variables for guaranteed violet character or weapon every 10 pull
    global legendary_pulls #take global variables for guaranteed legendary character every 90 pull

    global total_violet    #take global just a fuckin statistic
    global total_legendary #same shit
    global total_blue      #and same shit

    violet_pulls = violet_pulls + 1        #+1 to global number of pulls for guaranteed violet.
    legendary_pulls = legendary_pulls + 1  #+1 to global number of pulls for guarantedd legendary.

    pull = random.choices(['Легендарка', 'Фиол', 'Синька'], weights=[0.6, 5.1, 94.3]) #that's a random with weigth of chances to take (legendary 0.6%, violet 5.1%, blue 94.3%)

    if violet_pulls >= 10:
        pull = random.choices(['Легендарка', 'Фиол', 'Синька'], weights=[0.6, 99.4, 0]) #if pulls >= 10 give violet pull
                                                                                        #also we have chances to get legendary

    elif legendary_pulls >= 90:
        pull = random.choices(['Легендарка', 'Фиол', 'Синька'], weights=[100, 0, 0])    #same shit, if pulls >= 90 give legendary

    if pull == ['Синька']: #if we take a blue, give that random blue weapon.
        total_blue = total_blue + 1
        pull = random.choice([
            '(*3) Рогатка', '(*3) Лук ворона', '(*3) Эпос о драконоборцах', '(*3) Чёрная кисть', '(*3) Меч драконьей крови',
            '(*3) Меч небесного всадника', '(*3) Холодное лезвие', '(*3) Клятва стрелка', '(*3) Изумрудный шар', '(*3) Руководство по магии',
            '(*3) Дубина переговоров', '(*3) Металлическая тень', '(*3) Предвестник зари' 
        ])

    elif pull == ['Фиол']: #if we take violet
        violet_pulls = 0   #clear number of guaranteed pulls
        total_violet = total_violet + 1 #total violet

        hg = hero_or_gun() #call func to get random 50/50 weapon or character
        if hg == ['Герой']:#if character
            pull = random.choice([
                '(*4) Синь Янь', '(*4) Диона', '(*4) Ноэль', '(*4) Фишль', '(*4) Син Цю', '(*4) Сян Лин', '(*4) Рэйзор', '(*4) Барбара', #Персонажи
                '(*4) Сахароза', '(*4) Чун Юнь', '(*4) Беннет', '(*4) Нин Гуан', '(*4) Бэй Доу', '(*4) Эмбер', '(*4) Кэйа', '(*4) Лиза'
            ])
        else: #else weapon
            pull = random.choice([
                '(*4) Ржавый Лук', '(*4) Бесструнный', '(*4) Око сознания', '(*4) Песнь странника', '(*4) Копьё фавония', '(*4) Дождерез', '(*4) Меч-колокол', #Пушки
                '(*4) Драконий рык', '(*4) Меч-флейта', '(*4) Церемониальный лук', '(*4) Боевой лук фавония', '(*4) Ритуальные мемуары', '(*4) Кодекс фавония',
                '(*4) Гроза драконов', '(*4) Церемонимальный двуручный меч', '(*4) Двуручный меч фавония', '(*4) Церемонимальный меч', '(*4) Меч фавония'
            ])
        

    elif pull == ['Легендарка']: #if we get that's fucking pull

        legendary_pulls = 0      #clear legendary guaranteed counter
        total_legendary = total_legendary + 1

        print("   THAT'S FUCKING PULL! \n") #give message if we get legendary character
        hg = hero_or_gun() #call func 50/50 weapon or character
        if hg == ['Герой']:
            pull = random.choice([
                '(*5) Кэ Цин', '(*5) Ци Ци', '(*5) Джинн', '(*5) Мона', '(*5) Дилюк' #Лег персонажи.
            ])
        else:
            pull = random.choice([
                '(*5) Небесное крыло', '(*5) Небесный атлас', '(*5) Небесная ось', '(*5) Небесное величие', '(*5) Меч Сокола', #Лег пушки.
                '(*5) Лук Амоса', '(*5) Молитва святым ветрам', '(*5) Нефритовый коршун', '(*5) Волчья погибель', '(*5) Небесный меч'
            ])    

    pull = ("[" + str(pull) + "]") #just a for format message.

    return pull


def ten_pull(): #func for 10 pulls.
    tenPullStr = ''
    for n in range(10):
        tenPullStr = tenPullStr + str(one_pull() + "\n   ")
    return tenPullStr

def hundreed_pull(num_of_pulls): #func for >10 pulls
    tenPullStr = ''
    for n in range(num_of_pulls):
        tenPullStr = tenPullStr + str(one_pull() + "\n   ")
    return tenPullStr


while True: #cycle for menu
    print("")
    print("  Total pulls: " + str(x))
    print("  Until guaranteed violet: " + str(10 - violet_pulls))
    print("  Until guaranteed legendary: " + str(90 - legendary_pulls))
    print("")
    print("  Total: | " + str(total_legendary) + " Leg. | " + str(total_violet) + " Viol. | " + str(total_blue) + " Blue. |")
    print("\n\n   + The current sample shows:")
    print("")
    print("   | Legendary.  ~" + chance_on_legendary + "%")
    print("   | Violet. ~" + chance_on_violet + "%")
    print("   | Blue.  ~" + chance_on_blue + "%\n")
    print("")
    print("  How many wishes you wanna make? Pog")
    print("")
    print("    1 - One")
    print("    10 - Ten")
    print("    Or any number greater than ten. monkaS")
    print("")
    print("    0 - Clear statistic")
    print("")
    gacha = input("  Your choice: ")

    try: #catch errors
        gacha = int(gacha)
        os.system("cls")
        print("")

        if gacha == 1: #for one pull.
            x = x + 1
            print("  You wish " + str(x) + " times and you get:\n\n")
            print("   " + one_pull() + "\n")
            print("")
            

        elif gacha == 10: #for ten pulls.
            x = x + 10
            print("  You wish " + str(x) + " times and you get:\n\n")
            print("   " + ten_pull())
            print("")


        elif gacha > 10: #for >10 pulls.
            x = x + gacha
            print("  You wish " + str(x) + " times and you get:\n\n")
            print("   " + hundreed_pull(gacha))
            print("")


        elif gacha == 0: #clear statistic.

            tenPullStr = ""
            x = 0
            violet_pulls = 0
            legendary_pulls = 0

            total_violet = 0
            total_legendary = 0
            total_blue = 0

            chance_on_legendary = "0.6" #just a official chances.
            chance_on_violet = "5.1"
            chance_on_blue = "94.3"
            
            print("\n  Statistic cleared!\n")

        continX = input("  Press any key to continue...")
        os.system("cls")
        try:
            roundlegendary = round(((total_legendary / x) * 100), 3) #math, chances to get legendary.
            chance_on_legendary = str(roundlegendary)

            roundviolet = round(((total_violet / x) * 100), 3) #math, chances to get violet.
            chance_on_violet = str(roundviolet)

            roundblue = round(((total_blue / x) * 100), 3) #math, chances to get blue.
            chance_on_blue = str(roundblue)
        except ZeroDivisionError:
            os.system("cls")
    except ValueError:
        os.system("cls")
