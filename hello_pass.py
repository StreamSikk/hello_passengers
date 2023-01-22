import winsound as ws
import time
import os


clear = lambda: os.system('cls')

print("Добро пожаловать в HELLO PASSENGERS!")


def says_afl_1():

    print("===Сейчас играет: 1. Подготовка к вылету===")
    print()
    print('Воспроизводится: Добро пожаловать(1/2)')
    ws.PlaySound('AFL/1_or_departure/1_welcome.wav', ws.SND_FILENAME)
    clear()

    for i in range(1, 0, -1):
        i -= 1
        for o in range(10, 0, -1):
            print("===Сейчас играет: 1. Подготовка к вылету===")
            print()
            print(f'{i} минут {o} секунд осталось до след. проигрыша "Готовимся к взлету"(2/2)')
            time.sleep(1)
            clear()

    print("===Сейчас играет: 1. Подготовка к вылету===")
    print()
    print('Воспроизводится: Готовимся к взлету(2/2)')
    ws.PlaySound('AFL/1_or_departure/2_prepare.wav', ws.SND_FILENAME)
    clear()
    return '===ПРОИГРАНО==='

def says_afl_2():

    print("===Сейчас играет: 2. Выталкивание и руление===")
    print()
    print("Воспроизводится: Армировать двери(1/4)")
    ws.PlaySound('AFL/2_towing_taxiing/1_armed_door.wav')
    clear()

    for i in range (29, 0 , -1):
        print("===Сейчас играет: 2. Выталкивание и руление===")
        print()
        print(f'{i} осталось секунд до след. проигрыша "приведствие на боту"(2/4)')
        time.sleep(1)
        clear()

    print("===Сейчас играет: 2. Выталкивание и руление===")
    print()
    print("Воспроизводится: Приведствие на борту(2/4)")
    ws.PlaySound('AFL/2_towing_taxiing/2_greetings.wav')
    clear()

    for k in range (2, 0 , -1):
        k -= 1
        for i in range (59, 0 , -1):
            print("===Сейчас играет: 2. Выталкивание и руление===")
            print()
            print(f'{k} минут {i} секунд до след. проигрыша "аварийно-спасательное оборудование"(3/4)')
            time.sleep(1)
            clear()
    
    print("===Сейчас играет: 2. Выталкивание и руление===")
    print()
    print("Воспроизводится: аварийно-спасательное оборудование(3/4)")
    ws.PlaySound('AFL/2_towing_taxiing/3_pa_safety.wav')
    clear()

    for k in range (3, 0 , -1):
        k -= 1
        for i in range (59, 0 , -1):
            print("===Сейчас играет: 2. Выталкивание и руление===")
            print()
            print(f'{k} минут {i} секунд до след. проигрыша "рассказ аэрофлот бонус"(4/4)')
            time.sleep(1)
            clear()

    print("===Сейчас играет: 2. Выталкивание и руление===")
    print()
    print("Воспроизводится: аэрафлот бонус(4/4)")
    ws.PlaySound('AFL/2_towing_taxiing/3_pa_safety.wav')
    clear()
    return '===ПРОИГРАНО==='

def says_afl_3():

    print("===Сейчас играет: 3. Взлет и набор===")
    print
    print('Воспроизводится: Наш самолет готов к взлету(1/2)')
    ws.PlaySound('AFL/3_takeoff/1_ready_takeoff.wav')

    clear
    for k in range (8, 0 , -1):
        k -= 1
        for i in range (59, 0 , -1):
            print("===Сейчас играет: 3. Взлет и набор===")
            print()
            print(f'{k} минут {i} секунд до след. проигрыша "предложим закуски"(2/2)')
            time.sleep(1)
            clear()

    print("===Сейчас играет: 3. Взлет и набор===")
    print
    print('Воспроизводится: Предложим закуски"(2/2)')
    ws.PlaySound('AFL/3_takeoff/2_climb.wav')
    clear()
    return '===ПРОИГРАНО==='

def says_afl_4():

    print("===Сейчас играет: 4. Эшелон===")
    print
    print('Воспроизводится: Выключил табло(1/1)')
    ws.PlaySound('AFL/4_cruise/1_cruise.wav')
    clear()
    return '===ПРОИГРАНО==='

def says_afl_5():

    print("===Сейчас играет: 5. Снижение===")
    print
    print('Воспроизводится: Приступил к снижению(1/2)')
    ws.PlaySound('AFL/5_go_decline/1_go_decline.wav')

    for k in range (10, 0, -1):
        k -= 1
        for i in range (59, 0, -1):
            print("===Сейчас играет: 5. Снижение===")
            print()
            print(f'{k} минут {i} секунд до след. проигрыша "Заканчиваем обслуживание"(2/2)')
            time.sleep(1)
            clear()

    print("===Сейчас играет: 5. Снижение===")
    print
    print('Воспроизводится: Снижение(2/2)')
    ws.PlaySound('AFL/5_go_decline/2_to_land.wav')
    clear()
    return '===ПРОИГРАНО==='

def says_afl_6():

    print("===Сейчас играет: 5. Готов к посадке===")
    print
    print('Воспроизводится: Готов к посадке(1/1)')
    ws.PlaySound('AFL/6_landing/1_landing.wav')
    clear()
    return '===ПРОИГРАНО==='

def says_afl_7():

    print("===Сейчас играет: 7. Прибыл в место назначения===")
    print
    print('Воспроизводится: Совершил посадку(1/2)')
    ws.PlaySound('AFL/7_destination/1_destination.wav')

    for k in range (3, 0, -1):
        k -= 1
        for i in range (59, 0, -1):
            print("===Сейчас играет: 7. Место назначения===")
            print()
            print(f'{k} минут {i} секунд до след. проигрыша "Не вставать"(2/2)')
            time.sleep(1)
            clear()

    print("===Сейчас играет: 7. Прибыл в место назначение===")
    print
    print('Воспроизводится: Не вставать(2/2)')
    ws.PlaySound('AFL/7_destination/2_taxiing.wav')
    clear()
    return '===ПРОИГРАНО==='

def says_afl_8():

    print("===Сейчас играет: 8. Открыть двери===")
    print()
    print('Воспроизводится: Дизарм двери(1/1)')
    ws.PlaySound('AFL/8_end/1_disarmed_door.wav', ws.SND_FILENAME)
    clear()
    return '===ПРОИГРАНО==='

def says_afl_turb():
    print("===Сейчас играет: Турбулентность===")
    print()
    print('Воспроизводится: Турбулентность(1/1)')
    ws.PlaySound('AFL/turb.wav', ws.SND_FILENAME)
    clear()


while True:

    print(f"""
        ===МЕНЮ===

1. Речь: АЭРОФЛОТ | (AFL)
2. Речь: РОССИЯ | (SDM) | (В РАЗРАБОТКЕ)
""")

    menu_choicet = input("Введите цифру или ICAO: ")

    if menu_choicet == '1' or menu_choicet == 'AFL' or menu_choicet == 'afl':
        clear()
        play_afl = {}

        for i in range(0,9):
            play_afl[i] = "НЕ ПРОИГРАНО"

        exit_afl = True
        while exit_afl:
            print(F"""
            ===МЕНЮ РЕЧЬ АЭРОФЛОТА!===

1. Подготовка к вылету | {play_afl[0]}
2. Выталкивание и руление | {play_afl[1]}
3. Взлет и набор | {play_afl[2]}
4. Эшелон | {play_afl[3]}
5. Снижение | {play_afl[4]}
6. Готов к посадке | {play_afl[5]}
7. Прибыл в место назначения | {play_afl[6]}
8. Открыть двери | {play_afl[7]}
9. Турбуленция

Для выхода в меню: /menu
""")

            num_afl = input("Введите номер: ")

            if num_afl == "1":
                clear()
                play_afl[0] = says_afl_1()
                clear()

            elif num_afl == "2":
                clear()
                play_afl[1] = says_afl_2()
                clear()

            elif num_afl == "3":
                clear()
                play_afl[2] = says_afl_3()
                clear()

            elif num_afl == "4":
                clear()
                play_afl[3] = says_afl_4()
                clear()

            elif num_afl == "5":
                clear()
                play_afl[4] = says_afl_5()
                clear()

            elif num_afl == "6":
                clear()
                play_afl[5] = says_afl_6()
                clear()

            elif num_afl == "7":
                clear()
                play_afl[6] = says_afl_7()
                clear()

            elif num_afl == "8":
                clear()
                play_afl[7] = says_afl_8()
                clear()

            elif num_afl == "9":
                clear()
                play_afl[8] = says_afl_turb()
                clear()

            elif num_afl == "/menu":
                clear()
                break
            
            else:
                input("""
===Цифра не найдена!===""")
                clear()

    elif menu_choicet == '2' or menu_choicet == 'SDM' or menu_choicet == 'sdm':
        input('''
Речь РОССИИ в разработке!''')
        clear()


    else:
        input("""
===Не найдено!===""")
        clear()