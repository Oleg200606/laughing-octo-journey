import curses
import time
import json
import csv
import os 



def load_game():
    if os.path.exists('save.json'):
        with open('save.json', 'r') as f:
            return set(json.load(f))
    return set()


def save_to_csv(username):
    with open('game_data.csv',mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([username])
def save_hod(vibor):
    data = {'vibor': vibor}

    # Сохранение в CSV файл
    with open('game_data.csv', mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([vibor])
        data = {'vibor': vibor}
    
    # Сохранение в JSON файл
    with open('game_data.json', 'a') as json_file:
        json.dump(data, json_file)
        json_file.write('\n')

    



username = input("Введите ваше имя: ")


def main(stdscr):
    curses.curs_set(0)  
    stdscr.nodelay(1)  
    
    def sek(su):
        time.sleep(su)
    def nachalo(zhopa):
        return zhopa
    def wtoroe_nachlo(zhopenziya):
        return zhopenziya
    def poz(pozdr):
        return pozdr


    
    

    while True:
        

        stdscr.clear()
        stdscr.addstr(0, 0, nachalo("Игра Студентская жизнь!!! Жанр Новелла."), curses.A_BOLD)
        stdscr.addstr(1, 10, "Глава 1", curses.A_BOLD)
        stdscr.addstr(2, 0, "Если хотите начать игру сначала, нажмите 'y', если хотите выйти, нажмите 'q',", curses.A_NORMAL)
        stdscr.refresh()
       

        key = stdscr.getch()  
        if key == ord('y'):
            save_to_csv(username)
            save_hod("Нажата клавиша 'у',  ")
            stdscr.clear()
            stdscr.addstr(1, 50, wtoroe_nachlo("Игра началась! "), curses.A_BOLD)
            stdscr.refresh()
            sek(3)
            stdscr.clear()
            stdscr.addstr(1, 30, "Итак, вы поступили в университет", curses.A_BOLD)
            stdscr.refresh()
            sek(3)
            stdscr.addstr(3, 30, "В в течение недели вы разговорились со своим одногруппником", curses.A_BOLD)
            stdscr.refresh()
            sek(3)
            stdscr.addstr(5, 30, "И он вам предлагает дружить", curses.A_BOLD)
            stdscr.refresh()
            sek(3)
            stdscr.addstr(7, 30, "Вы приняли его предложение о дружбе.", curses.A_BOLD)
            stdscr.refresh()
            sek(3)
            stdscr.addstr(9, 30, "Теперь вам не будет скучно на парах.", curses.A_BOLD)
            stdscr.refresh()
            sek(3) 
            stdscr.addstr(11, 30, "Вы сидите, веселитесь, обсуждая совсем другие вещи, а не учёбу.", curses.A_BOLD)
            stdscr.refresh()
            sek(3) 
            stdscr.addstr(13, 30, "Но под конец первого семестра осознаёте, что у вас накопилась уйма долгов и надо что-то менять.", curses.A_BOLD)
            stdscr.refresh()
            sek(3)
            stdscr.addstr(15, 30, "И опять перед вами встаёт выбор, либо переставать общаться со своим уже лучшим ", curses.A_BOLD)
            stdscr.addstr(16, 30, "другом, либо поговорить с ним об этом, и вместе стараться выпутаться из долговой ямы", curses.A_BOLD)
            stdscr.refresh()
            sek(3)
            stdscr.addstr(18, 30, "Нажмите ”а”, чтобы продолжить дружить с ним или “s”, чтобы перестать с ним дружить", curses.A_BOLD)
            stdscr.refresh()
            while True:
                key = stdscr.getch() 
                if key == ord('a'):
                    save_hod("Нажата клавиша 'a',  ")
                    stdscr.clear()
                    stdscr.addstr(1, 20, "Вы проводите разговор с другом, и он соглашается с вашими представлениями об учёбе.", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(3, 20, "Вы вместе начинаете сдавать долги по предметам, тем самым исправляя ваши оценки по предметам.", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(5, 20, "Итак, дело близится к завершению. То есть к экзамену. ", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(7, 20, "За день до экзамена, ваш друг вас приглашает на вечеринку. ", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(9, 20, "Вы собирались этим вечером повторять весь пройденный материал за год. ", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(11, 20, "Но друг настаивает. ", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(13, 20, "Перед вами встаёт выбор, пойти с другом на вечеринку, не пойти на вечеринку, или отговорить друга ", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(15, 20, "Нажмите ”а”, чтобы пойти с ним или “s”, чтобы не идти и “d”, чтобы отговорить его.", curses.A_BOLD)
                    stdscr.refresh()
                    
                    while True:
                        key = stdscr.getch() 
                        if key == ord('a'):
                            save_hod("Нажата клавиша 'a',  ")
                            stdscr.clear() 
                            stdscr.addstr(1, 20, "Вы идёте на вечеринку и проводите отлично время.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(3, 20, "Приходите в 4 утра домой и пьяный ложитесь спать", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(5, 20, "И в 8 утра у вас звенит будильник.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(7, 20, "Вы ели-ели встаёте с дичайший похмельем, идете на кухню и выпиваете стакан воды с аспирином.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(9, 20, "Смотрите на время, и понимаете что экзамен начинается через полтора часа.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(11, 20, "Вы звоните другу, но он не отвечает.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(13, 20, "Ваш выбор, заехать за ним, но вы опоздаете или поехать самому и успеть.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(15, 20, "Нажмите ”а”, чтобы поехать за ним или “s”, чтобы поехать самому.", curses.A_BOLD)
                            stdscr.refresh()
                            
                            while True:
                                key = stdscr.getch() 
                                if key == ord('a'):
                                    save_hod("Нажата клавиша 'a',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы всё же решаете не бросать друга в биде, и едите к нему.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(3, 20, "Приехав к нему, вы залезете в подъезд через окно и поднимаетесь на его этаж.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(5, 20, "Вы стучите по его двери, как по боксёрской груше. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(7, 20, "И в итоге у вас получается его разбудить.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(9, 20, "Он в спешке одевается и вы едите на экзамен.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(11, 20, "Опоздав на экзамен вы ели-ели договариваетесь с учителем, чтобы тот допустил вас до экзамена.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(13, 20, "Итог: Вы с другом сдаёте экзамен на 3. И не совсем довольные идёте по домам.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(15, 20, "Вы закончили первый курс!!! \n Нажмите 'q' для выхода !!! ", curses.A_BOLD)
                                    stdscr.refresh()
                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            return 
                                    
                                    
                                elif key == ord('s'):
                                    save_hod("Нажата клавиша 's',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы едите на экзамен сами.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(3, 20, "Приезжаете туда, а вашего друга всё ещё нет. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(5, 20, "Вы пишете экзамен, получаете 4. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(7, 20, "Выходя из аудитории вы встречаете друга, который с грустной физиономией, ", curses.A_BOLD)
                                    stdscr.addstr(9, 20, "отворачивается от вас", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(11, 20, "Вам предстоит сделать выбор. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(13, 20, "Или вы идёте к другу, поддержать его, или идете  домой", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(15, 20, "Нажмите ”а”, чтобы пойти домой или “s”, чтобы подойти к другу.", curses.A_BOLD)
                                    stdscr.refresh()

                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('a'):
                                            save_hod("Нажата клавиша 'a',  ")
                                            stdscr.clear() 
                                            stdscr.addstr(1, 20, "Вы едите домой.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(3, 20, "Ваши отношения с другом на грани разрыва.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(5, 20, "Первый курс закончен!!!!!! \n Нажмите 'q' для выхода !!! ", curses.A_BOLD)
                                            stdscr.refresh()
                                            while True:
                                                key = stdscr.getch() 
                                                if key == ord('q'):
                                                    save_hod("Нажата клавиша 'q',  ")
                                                    return 
                                            
                                            
                                        elif key == ord('s'):
                                            save_hod("Нажата клавиша 's',  ")
                                            stdscr.clear() 
                                            stdscr.addstr(1, 20, "Вы подходите к другу. ", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(3, 20, "Он говорит вам, что из-за пропуска экзамена, он не перешел на 2 курс. ", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(5, 20, "Вы не знаете чем ему помочь.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(7, 20, "Для вас первый курс окончен. Поздравляю!!! \n Нажмите 'q' для выхода !!! ", curses.A_BOLD)
                                            stdscr.refresh()
                                            while True:
                                                key = stdscr.getch() 
                                                if key == ord('q'):
                                                        save_hod("Нажата клавиша 'q',  ")
                                                        return 
                                            
                                        elif key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            return 
                                elif key == ord('q'):
                                    save_hod("Нажата клавиша 'q',  ")
                                    return 
                                        
                        elif key == ord('s'):
                            save_hod("Нажата клавиша 's',  ")
                            stdscr.clear() 
                            stdscr.addstr(1, 20, "Вы остаётесь дома и занимаетесь подготовкой к экзамену. ", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)  
                            stdscr.addstr(3, 20, "На утро встаёте с хорошим предчувствием. ", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3) 
                            stdscr.addstr(5, 20, "Звоните другу, но он не берёт трубку", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(7, 20, "Ваш выбор, заехать за ним, но вы возможно опоздаете или поехать самому и точно успеть.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(9, 20, "Нажмите ”а”, чтобы поехать за ним или “s”, чтобы поехать самому.", curses.A_BOLD)
                            stdscr.refresh()
                            while True:
                                key = stdscr.getch() 
                                if key == ord('a'):
                                    save_hod("Нажата клавиша 'a',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы всё же решаете не бросать друга в биде, и едите к нему.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(3, 20, "Приехав к нему, вы залезете в подъезд через окно и поднимаетесь на его этаж.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(5, 20, "Вы стучите по его двери, как по боксёрской груше. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(7, 20, "И в итоге у вас получается его разбудить.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(9, 20, "Он в спешке одевается и вы едите на экзамен.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(11, 20, "Приезжаете на экзамен за 3 минуты.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(13, 20, "Врываетесь в аудиторию, испугав всех.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(15, 20, "Вы сдаёте экзамен на 5, но вашему другу ставят 3. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(17, 20, "Вы успешно закончили первый курс, оставшись в хороших отношениях с другом!!! \n Нажмите 'q' для выхода !!! ", curses.A_BOLD)
                                    stdscr.refresh()
                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            return 
                                    
                                elif key == ord('s'):
                                    save_hod("Нажата клавиша 's',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы едите на экзамен сами. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)  
                                    stdscr.addstr(3, 20, "Приезжаете туда, а вашего друга всё ещё нет. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3) 
                                    stdscr.addstr(5, 20, "Вы пишете экзамен, получаете 5. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(7, 20, "Выходя из аудитории вы встречаете друга, который с грустной физиономией.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3) 
                                    stdscr.addstr(9, 20, "Он отворачивается от вас.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(11, 20, "Вам предстоит сделать выбор.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(13, 20, "Или вы идёте к другу поддержать его, или идете домой", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(15, 20, "Нажмите ”а”, чтобы поехать домой или “s”, чтобы подойти к другу.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('a'):
                                            save_hod("Нажата клавиша 'a',  ")
                                            stdscr.clear() 
                                            stdscr.addstr(1, 20, "Вы едите домой.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(3, 20, "Ваши отношения с другом на грани разрыва.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(5, 20, "Первый курс закончен. \n Нажмите 'q' для выхода !!!  ", curses.A_BOLD)
                                            stdscr.refresh()
                                            while True:
                                                key = stdscr.getch() 
                                                if key == ord('q'):
                                                    save_hod("Нажата клавиша 'q',  ")
                                                    return 
                                            
                                        elif key == ord('s'):
                                            save_hod("Нажата клавиша 's',  ")
                                            stdscr.clear() 
                                            stdscr.addstr(1, 20, "Вы подходите к другу. ", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(3, 20, "Он говорит вам, что из-за пропуска экзамена, он не перешел на 2 курс. ", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(5, 20, "Вы не знаете чем ему помочь.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(7, 20, "Для вас первый курс окончен. Поздравляю!!! \n Нажмите 'q' для выхода !!! ", curses.A_BOLD)
                                            stdscr.refresh()
                                            while True:
                                                key = stdscr.getch() 
                                                if key == ord('q'):
                                                    save_hod("Нажата клавиша 'q',  ")
                                                    return 
                                            
                                        elif key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            
                                            return 
                        elif key == ord('d'):
                            save_hod("Нажата клавиша 'd',  ")
                            stdscr.clear() 
                            stdscr.addstr(1, 20, "У вас получается отговорить друга.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(3, 20, "И вы с ним приступаете к подготовке к экзамену. ", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(5, 20, "Успешно всё повторив, ложитесь спать. ", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)     
                            stdscr.addstr(7, 20, "С утра вы просыпаетесь с отличным настроением и уверенностью в предстоящем дне.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)     
                            stdscr.addstr(9, 20, "Вы звоните другу, и договариваетесь во сколько вы встретитесь с ним, тобы вместе", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)    
                            stdscr.addstr(11, 20, "поехать на экзамен.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)    
                            stdscr.addstr(13, 20, "Встретившись с другом, вы замечаете ребят, которые позвали вас на вечеринку. ", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(15, 20, "Вы можете подойти к ним и спросить “как дела”, либо поехать на экзамен.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)    
                            stdscr.addstr(17, 20, "Нажмите ”а”, чтобы поехать или “s”, чтобы подойти к ребятам.", curses.A_BOLD)
                            stdscr.refresh()
                            while True:
                                key = stdscr.getch() 
                                if key == ord('a'):
                                    save_hod("Нажата клавиша 'a',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы поехали на экзамен.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(3, 20, "Прибыв туда половины группы не было. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(5, 20, "Вы с другом успешно пишете экзамен, получаете 5. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(7, 20, "На этом счастливом моменте вы оканчиваете первый курс.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(9, 20, poz("Поздравляю \n Нажмите 'q' для выхода !!!")  , curses.A_BOLD)
                                    stdscr.refresh()
                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            return 
                                    
                                    
                                if key == ord('s'):
                                    save_hod("Нажата клавиша 's',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы подходите ребятам и спрашиваете как у них дела.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(3, 20, "Они отвечают, что совсем не готовы писать экзамен, так как на вчерашней вечеринке", curses.A_BOLD)
                                    stdscr.addstr(4, 20, "перебрали с алкоголем.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(6, 20, "Вы стараетесь их уговорить пойти на экзамен и у вас это получается.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(8, 20, "Тем самым вы пишете экзамен, получая оценку 5 вместе с другом. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(10, 20, "И ребята поняв, что если бы ты не подошел, то они не перевелись бы на 2 курс, благодарят", curses.A_BOLD)
                                    stdscr.addstr(12, 20, "тебя от всей души", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(14, 20, "Итог: Вы успешно заканчиваете 1 курс, и у вас появляется много друзей.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(16, 20,poz("Поздравляю \n Нажмите 'q' для выхода !!!"), curses.A_BOLD)
                                    stdscr.refresh()
                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            return 
                                    
                elif key == ord('s'):
                    save_hod("Нажата клавиша 's',  ")
                    stdscr.clear()
                    stdscr.addstr(1, 20, "Вы разрываете общение с другом.", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(3, 20, "Тем самым, буквально через пару месяцев, вы понимаете, что без друзей совсем не", curses.A_BOLD)
                    stdscr.addstr(4, 20, "хочется обучаться", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(6, 20, "В итоге перед вами встаёт выбор, либо найти себе нового друга, либо вернутся к старому.", curses.A_BOLD)
                    stdscr.refresh()
                    sek(3)
                    stdscr.addstr(8, 20, "Нажмите ”а”, чтобы найти новых друзей или “s”, чтобы вернуться ко старому.", curses.A_BOLD)
                    stdscr.refresh()
                    while True:
                        key = stdscr.getch() 
                        if key == ord('a'):
                            save_hod("Нажата клавиша 'a',  ")
                            stdscr.clear() 
                            stdscr.addstr(1, 20, "Вы находите себе нового друга.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(3, 20, "Но ваше общение заканчивается за пределами учебного заведения.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(5, 20, "Дело подходит к экзамену.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(7, 20, "За ночь до экзамена, всех приглашают на вечеринку, но вас нет. ", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(9, 20, "Перед вами стоит выбор, пойти ли вечеринку без приглашения, или остаться дома и", curses.A_BOLD)
                            stdscr.addstr(10, 20, "заняться подготовкой к экзамену.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(12, 20, "Нажмите ”а”, чтобы пойти или “s”, чтобы остаться дома.", curses.A_BOLD)
                            stdscr.refresh()
                            while True:
                                key = stdscr.getch() 
                                if key == ord('a'):
                                    save_hod("Нажата клавиша 'a',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы идете на вечеринку и встречаете там друга.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(3, 20, "Вы начинаете начинаете с ним разговор. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(5, 20, "И выясняется то, что у него тоже нет настоящих друзей.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(7, 20, "Вы на вечеринке проводите отлично время.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(9, 20, "Приходите в 4 утра домой и пьяный ложитесь спать.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(11, 20, "И в 8 утра у вас звенит будильник.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(13, 20, "Вы ели-ели встаёте с дичайший перегаром, идете на кухню и выпиваете стакан воды с ", curses.A_BOLD)
                                    stdscr.addstr(14, 20, "аспирином.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(16, 20, "Смотрите на время, и понимаете что экзамен начинается через полтора часа.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(18, 20, "Вы звоните другу, но он не отвечает.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(20, 20, "Ваш выбор, заехать за ним, но вы  опоздаете или поехать самому и успеть.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(22, 20, "Нажмите ”а”, чтобы поехать за ним или “s”, чтобы поехать самому.", curses.A_BOLD)
                                    stdscr.refresh()
                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('a'):
                                            save_hod("Нажата клавиша 'a',  ")
                                            stdscr.clear() 
                                            stdscr.addstr(1, 20, "Вы всё же решаете не бросать друга в биде, и едите к нему.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(3, 20, "Приехав к нему, вы залезете в подъезд через окно и поднимаетесь на его этаж.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(5, 20, "Вы стучите по его двери, как по боксёрской груше.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(7, 20, "И в итоге у вас получается его разбудить. ", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(9, 20, "Он в спешке одевается и вы едите на экзамен.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(11, 20, "Опоздав на экзамен вы ели-ели договариваетесь с учителем, чтобы тот допустил вас до", curses.A_BOLD)
                                            stdscr.addstr(12, 20, "экзамена.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(14, 20, "Итог: Вы сдаёте экзамен на 4, а ваш друг на 3. И довольные идёте по домам.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(16, 20, "Вы закончили первый курс!!!  \n Нажмите 'q' для выхода !!!", curses.A_BOLD)
                                            stdscr.refresh()
                                            while True:
                                                key = stdscr.getch() 
                                                if key == ord('q'):
                                                    save_hod("Нажата клавиша 'q',  ")
                                                    return 
                                            
                                        elif key == ord('s'):
                                            save_hod("Нажата клавиша 's',  ")
                                            stdscr.clear() 
                                            stdscr.addstr(18, 20, "Вы едите на экзамен сами.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(20, 20, "На экзамене нету пол группы включая вашего бывшего друга.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(22, 20, "Вы пишете экзамен, получаете 4.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(24, 20, "Для вас первый курс окончен. Поздравляю!!! \n Нажмите 'q' для выхода !!!", curses.A_BOLD)
                                            stdscr.refresh()
                                            while True:
                                                key = stdscr.getch() 
                                                if key == ord('q'):
                                                    save_hod("Нажата клавиша 'q',  ")
                                                    return 
                                            
                                        elif key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            
                                            return 
                                elif key == ord('s'):
                                    save_hod("Нажата клавиша 's',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы остаётесь дома.", curses.A_BOLD)
                                    stdscr.refresh()  
                                    sek(3)
                                    stdscr.addstr(3, 20, "Весь вечер вы тратите на подготовку к экзамену.", curses.A_BOLD)
                                    stdscr.refresh()  
                                    sek(3)           
                                    stdscr.addstr(5, 20, "С утра встаёте с хорошим настроением.", curses.A_BOLD)
                                    stdscr.refresh()  
                                    sek(3)   
                                    stdscr.addstr(7, 20, "Едите на экзамен.", curses.A_BOLD)
                                    stdscr.refresh()  
                                    sek(3)
                                    stdscr.addstr(9, 20, "Приехав, вы замечаете, что нету половины группы.", curses.A_BOLD)
                                    stdscr.refresh()  
                                    sek(3)  
                                    stdscr.addstr(11, 20, "Вы спрашиваете у старосты, но она сама не знает в чём дело.", curses.A_BOLD)
                                    stdscr.refresh()  
                                    sek(3) 
                                    stdscr.addstr(13, 20, "Вы отбрасываете этот вопрос на второй план и сосредотачиваетесь на экзамене.", curses.A_BOLD)
                                    stdscr.refresh()  
                                    sek(3)   
                                    stdscr.addstr(15, 20, "Итог: Bы успешно сдаёте экзамен и получаете 5 баллов.", curses.A_BOLD)
                                    stdscr.refresh()  
                                    sek(3) 
                                    stdscr.addstr(17, 20, "Поздравляю!! Вы перешли на 2 курс. \n Нажмите 'q' для выхода !!!", curses.A_BOLD)
                                    stdscr.refresh()  
                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            return 
                                    
                                elif key == ord('q'):
                                    save_hod("Нажата клавиша 'q',  ")
                                    
                                    return           

                                    

                        elif key == ord('s'):
                            save_hod("Нажата клавиша 's',  ")
                            stdscr.clear() 
                            stdscr.addstr(1, 20, "Вы решаетесь пойти поговорить со своим бывшим другом.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(3, 20, "Вы подходите к нему, и предлагаете опять дружить ", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)     
                            stdscr.addstr(5, 20, "Он соглашается.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3) 
                            stdscr.addstr(7, 20, "Вам становится намного легче, вы опять чувствуете себя прекрасно, потому что у вас есть", curses.A_BOLD)
                            stdscr.addstr(8, 20, "настоящий друг.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(10, 20, "Дело близится к экзамену, остался один день. ", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3) 
                            stdscr.addstr(11, 20, "Вам друг предлагает сходить в кино, но вы планировали провести этот вечер за ", curses.A_BOLD)
                            stdscr.addstr(12, 20, "подготовкой к экзамену", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(14, 20, "Перед вами стоит выбор, либо пойти с ним в кино, либо предложить заняться подготовкой.", curses.A_BOLD)
                            stdscr.refresh()
                            sek(3)
                            stdscr.addstr(16, 20, "Нажмите ”а”, чтобы пойти с ним или “s”, чтобы предложить свою идею.", curses.A_BOLD)
                            stdscr.refresh()
                        
                            while True:
                                key = stdscr.getch() 
                                if key == ord('a'):
                                    save_hod("Нажата клавиша 'a',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы идёте в кино и отлично проводите там время.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(3, 20, "Вернувшись домой, вы осознаёте почти не готовы к экзамену", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(5, 20, "На утро вы встаёте и едите на экзамен.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(7, 20, "Приехав на экзамен не можете найти своего друга.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(9, 20, "Начинаете ему звонить, он отвечает на звонок, и говорит что опаздывает на 5 минут.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(11, 20, "Но вы зная преподавателя понимаете, что друга могут не пустить на экзамен.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(13, 20, "Перед вами встаёт выбор, либо сидеть ждать экзамена, либо отвлекать учителя.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(15, 20, "Нажмите ”а”, чтобы ждать или “s”, чтобы отвлекать.", curses.A_BOLD)
                                    stdscr.refresh()
                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('a'):
                                            save_hod("Нажата клавиша 'a',  ")
                                            stdscr.clear() 
                                            stdscr.addstr(1, 20, "Экзамен начался.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(3, 20, "Ваш друг опаздывает и преподаватель пускает его на экзамен с учётом снижения на балл", curses.A_BOLD)
                                            stdscr.addstr(4, 20, "от оценки.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(6, 20, "Итог: вы получаете оценку 4, а ваш друг 3. Вы переходите на 2 курс.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(8, 20, poz("Поздравляю \n Нажмите 'q' для выхода !!!"), curses.A_BOLD)
                                            stdscr.refresh()
                                            while True:
                                                key = stdscr.getch() 
                                                if key == ord('q'):
                                                    save_hod("Нажата клавиша 'q',  ")
                                                    return 
                                            
                                            
                                        elif key == ord('s'):
                                            save_hod("Нажата клавиша 's',  ")
                                            stdscr.clear() 
                                            stdscr.addstr(1, 20, "Вы стараетесь всячески отвлечь преподавателя.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(3, 20, "И у вас это успешно получается.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(5, 20, "В итоге преподаватель не замечает, что ваш друг опоздал.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(7, 20, "Экзамен окончен, Вы с другом получаете оценку 4.", curses.A_BOLD)
                                            stdscr.refresh()
                                            sek(3)
                                            stdscr.addstr(9, 20, poz("Поздравляю \n Нажмите 'q' для выхода !!! "), curses.A_BOLD)
                                            while True:
                                                key = stdscr.getch() 
                                                if key == ord('q'):
                                                    save_hod("Нажата клавиша 'q',  ")
                                                    return 
                                        
                                        elif key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            return 
                                        
                                elif key == ord('s'):
                                    save_hod("Нажата клавиша 's',  ")
                                    stdscr.clear() 
                                    stdscr.addstr(1, 20, "Вы Говорите другу, что было бы лучше заняться подготовкой к экзамену.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(3, 20, "Он соглашается.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(5, 20, "И вы весь вечер подготавливаетесь к экзамену.", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(7, 20, "На следующий день вы с другом приходите на экзамен. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(9, 20, "И получаете свою заслуженную 5, а друг 4", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(11, 20, "Вы переходите на 2 курс. ", curses.A_BOLD)
                                    stdscr.refresh()
                                    sek(3)
                                    stdscr.addstr(13, 20, poz("Поздравляю \n Нажмите 'q' для выхода !!!"), curses.A_BOLD)
                                    stdscr.refresh()
                                    while True:
                                        key = stdscr.getch() 
                                        if key == ord('q'):
                                            save_hod("Нажата клавиша 'q',  ")
                                            return 
                                    
                                elif key == ord('q'):
                                    save_hod("Нажата клавиша 'q',  ")
                                    return 
        elif key == ord('q'):
            save_hod("Нажата клавиша 'q',  ")
            return
  
            
        
        
         
    

if __name__ == "__main__":
    curses.wrapper(main)
   