import random
import codecs
import json
import time
import os
from tqdm import tqdm, tqdm_gui, trange

os.system("cls") #win terminal clear

tenPullStr = "" #string for pulls in func "one_pull()"
wishes = 0
violet_pulls = 0
legendary_pulls = 0

total_violet = 0 #total leg, viol, blue shit
total_legendary = 0
total_blue = 0

chance_on_legendary = 0.6 #official chances to get leg, viol, blue shit
chance_on_violet = 5.1
chance_on_blue = 94.3

percent_of_legendary = 0
percent_of_violet = 0
percent_of_blue = 0

table_of_drop = []

def system_color(code_color): #win terminal color func
    os.system("color 0{0}".format(code_color))
    return None

def system_title(title_name): #win terminal title func
    os.system("title {0}".format(title_name))
    return None


system_title("Genshin Gacha - ANALyze") #win terminal title set

def hero_or_gun(): #50/50 func for gun or hero
    herogun = random.choices(['Герой', 'Оружие'], weights=[50, 50])
    return herogun

def one_pull(): #one pull func

    """
        just a global variables
    """
    global violet_pulls
    global legendary_pulls
    global total_violet
    global total_legendary
    global total_blue
    global chance_on_legendary
    global chance_on_violet
    global table_of_drop

    violet_pulls += 1 #count pulls for guaranteed violet
    legendary_pulls += 1 #count pulls for guaranteed legendary
    chance_on_legendary += 0.01105 #soft pity% for legendary
    chance_on_violet += 0.2922 #soft pity% for violet

    pull = random.choices(['Легендарка', 'Фиол', 'Синька'], weights=[chance_on_legendary, chance_on_violet, chance_on_blue]) #random pull with height 0.6%, 5,1% + soft pity

    if violet_pulls > 9: #if > 9 give violet
        pull = random.choices(['Легендарка', 'Фиол', 'Синька'], weights=[0.6, 99.4, 0])

    elif legendary_pulls > 89: #elif > 89 give legendary
        pull = random.choices(['Легендарка', 'Фиол', 'Синька'], weights=[100, 0, 0])

    if pull == ['Синька']: #if we get blue

        total_blue += 1
        pull = random.choice([
            '(*3) Рогатка', '(*3) Лук ворона', '(*3) Эпос о драконоборцах', '(*3) Чёрная кисть', '(*3) Меч драконьей крови',
            '(*3) Меч небесного всадника', '(*3) Холодное лезвие', '(*3) Клятва стрелка', '(*3) Изумрудный шар', '(*3) Руководство по магии',
            '(*3) Дубина переговоров', '(*3) Металлическая тень', '(*3) Предвестник зари' 
        ])

    elif pull == ['Фиол']: #if we get violet

        violet_pulls = 0   #clear numbers for guaranteed violet
        total_violet += 1
        chance_on_violet = 5.1

        hg = hero_or_gun() #50/50 func call
        if hg == ['Герой']:
            pull = random.choice([ #characters
                '(*4) Синь Янь', '(*4) Диона', '(*4) Ноэль', '(*4) Фишль', '(*4) Син Цю', '(*4) Сян Лин', '(*4) Рэйзор', '(*4) Барбара',
                '(*4) Сахароза', '(*4) Чун Юнь', '(*4) Беннет', '(*4) Нин Гуан', '(*4) Бэй Доу', '(*4) Эмбер', '(*4) Кэйа', '(*4) Лиза'
            ])
        else:
            pull = random.choice([ #weapons
                '(*4) Ржавый Лук', '(*4) Бесструнный', '(*4) Око сознания', '(*4) Песнь странника', '(*4) Копьё фавония', '(*4) Дождерез', '(*4) Меч-колокол',
                '(*4) Драконий рык', '(*4) Меч-флейта', '(*4) Церемониальный лук', '(*4) Боевой лук фавония', '(*4) Ритуальные мемуары', '(*4) Кодекс фавония',
                '(*4) Гроза драконов', '(*4) Церемонимальный двуручный меч', '(*4) Двуручный меч фавония', '(*4) Церемонимальный меч', '(*4) Меч фавония'
            ])
        pull = (" -> " + pull.upper())
        

    elif pull == ['Легендарка']: #if we get legendary

        legendary_pulls = 0 #clear numbers for guaranteed legendary
        total_legendary += 1
        chance_on_legendary = 0.6

        hg = hero_or_gun() #50/50 func call
        if hg == ['Герой']:
            pull = random.choice([ #legendary characters
                '(*5) Кэ Цин', '(*5) Ци Ци', '(*5) Джинн', '(*5) Мона', '(*5) Дилюк'
            ])
        else:
            pull = random.choice([ #legendary weapons
                '(*5) Небесное крыло', '(*5) Небесный атлас', '(*5) Небесная ось', '(*5) Небесное величие', '(*5) Меч Сокола',
                '(*5) Лук Амоса', '(*5) Молитва святым ветрам', '(*5) Нефритовый коршун', '(*5) Волчья погибель', '(*5) Небесный меч'
            ])    
        pull = (" -> " + pull.upper() + " <- ") #visualization for legendary

    table_of_drop.append(pull)
    return pull


def ten_pull(): #func for 10 pulls/wishes
    tenPullStr = ''
    pull_var = ['','','','','','','','','','']
    pull_max = []
    for i in range(10):
        one_pull_var = one_pull()
        pull_var[i] = one_pull_var
        if one_pull_var[6:7].isnumeric():
            pull_max.append(int(one_pull_var[6:7]))
        tenPullStr = tenPullStr + str(pull_var[i] + "\n   ")

    if int(max(pull_max)) == 5:
        system_color("6") #call func, change win terminal color for legendary pull!
        system_title("Genshin Gacha - ANALyze - 5* LEGENDARY! OH MY GOD!") #call func, change win terminal title!
    elif int(max(pull_max)) == 4:
        system_color("5") #call func, change win terminal color for violet pull!
        system_title("Genshin Gacha - ANALyze - 4* Violet!") #call func, change win terminal title!

    return tenPullStr

def hundreed_pull(num_of_pulls): #func 10+ pulls
    tenPullStr = ''
    for i in tqdm(range(num_of_pulls), desc='  Прогресс молитв', unit=' молитв' ):
        tenPullStr = tenPullStr + str(one_pull() + "\n   ")
    return tenPullStr

def clear_stat():
    global violet_pulls
    global legendary_pulls
    global total_violet
    global total_legendary
    global total_blue
    global chance_on_legendary
    global chance_on_violet
    global table_of_drop
    global tenPullStr
    global wishes
    global chance_on_blue
    global percent_of_legendary
    global percent_of_violet
    global percent_of_blue

    tenPullStr = ""
    wishes = 0
    violet_pulls = 0
    legendary_pulls = 0

    total_violet = 0
    total_legendary = 0
    total_blue = 0

    chance_on_legendary = 0.6
    chance_on_violet = 5.1
    chance_on_blue = 94.3

    percent_of_legendary = 0
    percent_of_violet = 0
    percent_of_blue = 0

    table_of_drop = []
            
    print("\n  Сброс молитв и статистики завершён!\n")
    return None

def get_time(): #time func
    t_time = time.strftime("%d-%B-%Y %H-%M-%S", time.localtime())
    return t_time

def export_drop(): #export drop and stats in json format .txt file
    get_time_for_file = get_time()
    with codecs.open('{1} - Молитв - {0} - Drop.txt'.format(get_time_for_file, wishes), 'w', encoding='utf-8') as fw:
        json.dump(table_of_drop, fw, ensure_ascii=False, indent=2)

    print("\n  Экспорт дропа завершён. И находится в файле: {1} - Молитв - {0} - Drop.txt".format(get_time_for_file, wishes))

    with codecs.open('{1} - Молитв - {0} - Stats.txt'.format(get_time_for_file, wishes), 'w', encoding='utf-8') as fw:

        table_of_stats = []
        table_of_stats.append("Вы покрутили: " + str(wishes))
        table_of_stats.append("До гаранта Фиолки: " + str(10 - violet_pulls))
        table_of_stats.append("До гаранта Легендарки: " + str(90 - legendary_pulls))
        table_of_stats.append("")
        table_of_stats.append("В общей сумме вам выпало: | " + str(total_legendary) + " Лег. | " + str(total_violet) + " Фиол. | " + str(total_blue) + " Син. |")
        table_of_stats.append("")
        table_of_stats.append("Проценты выпадения редких вещей на " + str(wishes) + " молитв:")
        table_of_stats.append("Лег.  ~" + str(percent_of_legendary) + "%")
        table_of_stats.append("Фиол. ~" + str(percent_of_violet) + "%")
        table_of_stats.append("Син.  ~" + str(percent_of_blue) + "%")

        json.dump(table_of_stats, fw, ensure_ascii=False, indent=2)

    print("  Экспорт статистики завершён. И находится в файле: {1} - Молитв - {0} - Stats.txt\n".format(get_time_for_file, wishes))

while True: #cycle for stats and menu choice
    system_color("f") #call func, change win terminal color
    system_title("Genshin Gacha - ANALyze - Menu") #call func, change win terminal title

    print("")
    print("  Вы покрутили: " + str(wishes))
    print("  До гаранта Фиолки: " + str(10 - violet_pulls))
    print("  До гаранта Легендарки: " + str(90 - legendary_pulls))
    print("")
    print("  В общей сумме вам выпало: | " + str(total_legendary) + " Лег. | " + str(total_violet) + " Фиол. | " + str(total_blue) + " Син. |")
    print("\n\n   + Проценты выпадения редких вещей на " + str(wishes) + " молитв:")
    print("")
    print("   | Лег.  ~" + str(percent_of_legendary) + "%")
    print("   | Фиол. ~" + str(percent_of_violet) + "%")
    print("   | Син.  ~" + str(percent_of_blue) + "%\n")

    #print("   | DEBUG LEG: " + str(chance_on_legendary) + "") #just a print debug for soft pity%
    #print("   | DEBUG VIO: " + str(chance_on_violet) + "\n")

    print("")
    print("  Сколько гач крутим? Pog")
    print("   +----+---------------+-------------------------+")
    print("   |  1 | Одну          | (*с отображением лута)  |")
    print("   | 10 | Десять        | (*с отображением лута)  |")
    print("   | 11 | Любое число+  | (*без отображения лута) |") #10+ pulls
    print("   +----+---------------+-------------------------+")
    print("   |  5 | Выгрузить списки дропа и статистики     |")
    print("   |  0 | Сброс статистики и количества молитв    |")
    print("   +----+-----------------------------------------+")
    print("")
    gacha = input("  Ваш выбор: ")

    try: #Catch errors
        gacha = int(gacha)
        os.system("cls")
        print("")

        if gacha == 1:
            wishes = wishes + 1
            print("  Вы молитесь " + str(gacha) + " раз и вам выпадает:\n\n")
            print("   " + one_pull() + "\n")
            print("")
            

        elif gacha == 10:
            wishes = wishes + 10
            print("  Вы молитесь " + str(gacha) + " раз/а и вам выпадает:\n\n")
            print("   " + ten_pull())
            print("")


        elif gacha > 10: #10+ pulls ellif for call func
            system_color("4") #call func, change win terminal color for violet pull!
            system_title("Genshin Gacha - ANALyze - Load {0} wishes...".format(gacha)) #call func, change win terminal title!
            wishes = wishes + gacha
            print("  Вы молитесь " + str(gacha) + " раз.\n")
            hundreed_pull(gacha)
            print("")

        elif gacha == 5:
            export_drop()

        elif gacha == 0: #clear stats
            clear_stat()

        continX = input("  Нажмите любую клавишу, чтобы продолжить...")
        os.system("cls")

        try: #catch errors
            roundlegendary = round(((total_legendary / wishes) * 100), 2) #simple math for total %
            percent_of_legendary = str(roundlegendary)

            roundviolet = round(((total_violet / wishes) * 100), 2)
            percent_of_violet = str(roundviolet)

            roundblue = round(((total_blue / wishes) * 100), 2)
            percent_of_blue = str(roundblue)

        except ZeroDivisionError:
            os.system("cls")

    except ValueError:
        os.system("cls")