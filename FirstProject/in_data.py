def indata():
    fam = str("Фамилия: " + input('Введите фамилию: '))
    name = str("Имя: " + input('Введите имя: '))
    num  = str("Номер: " + input('Введите номер: '))
    com = str("Комментарий: " + input('Введите комментарий: '))
    id = (fam, name, num, com)
    return id#(fam, name, num, com)

##def view_data(data):
##    print(f'result={data}')

##print(indata())