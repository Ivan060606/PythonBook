import in_data, log

def button_click():
    print('Введите "1" чтобы записать или "0" чтобы прочитать')
    flag = int(input())
    while flag == 1:
        while flag == 1:
            log.logger(in_data.indata())
            print('Введите "1" чтобы продолжить или "0" чтобы завершить')
            flag = int(input())
        print('Завершили ввод.')
        print('Введите "1" чтобы записать или "0" чтобы прочитать')
        flag = int(input())
    log.reader()