import random
import os
from tqdm import tqdm, tqdm_gui, trange

os.system("cls") #Делаем стартовую консоль красивее
os.system("title Genshin Gacha ANALyze") #Задаём имя для консоли

tenPullStr = "" #Ну тут чисто переменные всякие, какие то вызываются в функциях
x = 0
violet_pulls = 0
legendary_pulls = 0

total_violet = 0    #Количество выбитого дерьма
total_legendary = 0
total_blue = 0

chance_on_legendary = "0.6" #Шансы на одиночные гача крутки
chance_on_violet = "5.1"
chance_on_blue = "94.3"

def hero_or_gun():
    herogun = random.choices(['Герой', 'Оружие'], weights=[50, 50]) #Функция 50/50 определяющая герой или пушка
    return herogun

def one_pull():

    global violet_pulls    #Вызов глобальных переменных, данные переменные необходимы для выдачи гарантированных персонажей
    global legendary_pulls #Например если игроку не везёт, то на 90-ый ролл, он получит гарантировано легендарного персонажа

    global total_violet
    global total_legendary #Подсчет общего количества персонажей и пушек для статистики и определения ~реального шанса, с учетом гарантов и т.п.
    global total_blue

    violet_pulls = violet_pulls + 1        #Когда мы делаем пул, плюсуем в оба счетчика, по достижени отметки в 10 или 90
    legendary_pulls = legendary_pulls + 1  #Даём соответственно фиол/лег персонажа.

    pull = random.choices(['Легендарка', 'Фиол', 'Синька'], weights=[0.6, 5.1, 94.3]) #Это выбор на каждый пул, что нам упадёт (офф шансы на каждый единичный пул)

    if violet_pulls >= 10:
        pull = random.choices(['Легендарка', 'Фиол', 'Синька'], weights=[0.6, 99.4, 0]) #Если количество пулов =10, обнуляем счетчик для фиол перса и выдаем его.
                                                                                        #Также тут учитывается, шанс получить легендарного персонажа, всё те-же 0.6%

    elif legendary_pulls >= 90:
        pull = random.choices(['Легендарка', 'Фиол', 'Синька'], weights=[100, 0, 0])    #same thing, если счетчик =90, выдаем легу.

    if pull == ['Синька']: #Если падает синее, выдаем.
        total_blue = total_blue + 1
        pull = random.choice([
            '(*3) Рогатка', '(*3) Лук ворона', '(*3) Эпос о драконоборцах', '(*3) Чёрная кисть', '(*3) Меч драконьей крови',
            '(*3) Меч небесного всадника', '(*3) Холодное лезвие', '(*3) Клятва стрелка', '(*3) Изумрудный шар', '(*3) Руководство по магии',
            '(*3) Дубина переговоров', '(*3) Металлическая тень', '(*3) Предвестник зари' 
        ])

    elif pull == ['Фиол']: #Если падает фиол, 
        violet_pulls = 0   #обнуляем счетчик гаранта на фиол.
        total_violet = total_violet + 1

        hg = hero_or_gun() #50/50 пушка или персонаж.
        if hg == ['Герой']:
            pull = random.choice([
                '(*4) Синь Янь', '(*4) Диона', '(*4) Ноэль', '(*4) Фишль', '(*4) Син Цю', '(*4) Сян Лин', '(*4) Рэйзор', '(*4) Барбара', #Персонажи
                '(*4) Сахароза', '(*4) Чун Юнь', '(*4) Беннет', '(*4) Нин Гуан', '(*4) Бэй Доу', '(*4) Эмбер', '(*4) Кэйа', '(*4) Лиза'
            ])
        else:
            pull = random.choice([
                '(*4) Ржавый Лук', '(*4) Бесструнный', '(*4) Око сознания', '(*4) Песнь странника', '(*4) Копьё фавония', '(*4) Дождерез', '(*4) Меч-колокол', #Пушки
                '(*4) Драконий рык', '(*4) Меч-флейта', '(*4) Церемониальный лук', '(*4) Боевой лук фавония', '(*4) Ритуальные мемуары', '(*4) Кодекс фавония',
                '(*4) Гроза драконов', '(*4) Церемонимальный двуручный меч', '(*4) Двуручный меч фавония', '(*4) Церемонимальный меч', '(*4) Меч фавония'
            ])
        

    elif pull == ['Легендарка']: #Если падает лега,

        legendary_pulls = 0      #обнуляем счетчик гаранта на легу.
        total_legendary = total_legendary + 1

        hg = hero_or_gun() #Опять же 50/50 персонаж или пушка.
        if hg == ['Герой']:
            pull = random.choice([
                '(*5) Кэ Цин', '(*5) Ци Ци', '(*5) Джинн', '(*5) Мона', '(*5) Дилюк' #Лег персонажи.
            ])
        else:
            pull = random.choice([
                '(*5) Небесное крыло', '(*5) Небесный атлас', '(*5) Небесная ось', '(*5) Небесное величие', '(*5) Меч Сокола', #Лег пушки.
                '(*5) Лук Амоса', '(*5) Молитва святым ветрам', '(*5) Нефритовый коршун', '(*5) Волчья погибель', '(*5) Небесный меч'
            ])    

    pull = ("[" + str(pull) + "]") #Просто для красоты, делаем скобочки.

    return pull


def ten_pull(): #Функция на 10 пулов
    tenPullStr = ''
    for n in range(10):
        tenPullStr = tenPullStr + str(one_pull() + "\n   ")
    return tenPullStr

def hundreed_pull(num_of_pulls): #Функция на 10+ пулов.
    tenPullStr = ''
    for n in tqdm(range(num_of_pulls), desc='  Прогресс молитв', unit=' молитв' ):
        tenPullStr = tenPullStr + str(one_pull() + "\n   ")
    return tenPullStr


while True: #Цикл для меню со статистикой и выбором количество прокруток.
    print("")
    print("  Вы покрутили: " + str(x))
    print("  До гаранта Фиолки: " + str(10 - violet_pulls))
    print("  До гаранта Легендарки: " + str(90 - legendary_pulls))
    print("")
    print("  В общей сумме вам выпало: | " + str(total_legendary) + " Лег. | " + str(total_violet) + " Фиол. | " + str(total_blue) + " Син. |")
    print("\n\n   + Текущая выборка показывает, шансы на:")
    print("")
    print("   | Лег.  ~" + chance_on_legendary + "%")
    print("   | Фиол. ~" + chance_on_violet + "%")
    print("   | Син.  ~" + chance_on_blue + "%\n")
    print("")
    print("  Сколько гач крутим? Pog")
    print("")
    print("    1 - Одну")
    print("    10 - Десять")
    print("    Или любое число выше 10-ти. monkaS")
    print("")
    print("    0 - Сбросить статистику и количество молитв")
    print("")
    gacha = input("  Ваш выбор: ")

    try: #Ловим ошибки
        gacha = int(gacha)
        os.system("cls")
        print("")

        if gacha == 1: #Если выбрали один пул
            x = x + 1
            print("  Вы молитесь " + str(gacha) + " раз и вам выпадает:\n\n")
            print("   " + one_pull() + "\n")
            print("")
            

        elif gacha == 10: #Если выбрали десять пуллов
            x = x + 10
            print("  Вы молитесь " + str(gacha) + " раз/а и вам выпадает:\n\n")
            print("   " + ten_pull())
            print("")


        elif gacha > 10: #Если выбрали больше 10-ти.
            x = x + gacha
            print("  Вы молитесь " + str(gacha) + " раз.\n")
            hundreed_pull(gacha) #ЗДЕСЬ УБРАН PRINT, ДЛЯ ПРОСТОГО ОТОБРАЖЕНИЯ ПРОГРЕССА, АДАПТИРОВАНО ПОД СИМУЛЯЦИЮ И ПОДСЧЕТА СТАТИСТИКИ
            print("")


        elif gacha == 0: #Очистка статистики.

            tenPullStr = ""
            x = 0
            violet_pulls = 0
            legendary_pulls = 0

            total_violet = 0
            total_legendary = 0
            total_blue = 0

            chance_on_legendary = "0.6" #Возвращаем в статистику изначальные шансы.
            chance_on_violet = "5.1"
            chance_on_blue = "94.3"
            
            print("\n  Сброс молитв и статистики завершён!\n")

        continX = input("  Нажмите любую клавишу, чтобы продолжить...")
        os.system("cls")
        try:
            roundlegendary = round(((total_legendary / x) * 100), 3) #Расчет реального процента с учетом гаранта и округление
            chance_on_legendary = str(roundlegendary)

            roundviolet = round(((total_violet / x) * 100), 3) #Расчет реального процента с учетом гаранта и округление
            chance_on_violet = str(roundviolet)

            roundblue = round(((total_blue / x) * 100), 3) #Расчет реального процента с учетом гаранта и округление
            chance_on_blue = str(roundblue)
        except ZeroDivisionError:
            os.system("cls")
    except ValueError:
        os.system("cls")
