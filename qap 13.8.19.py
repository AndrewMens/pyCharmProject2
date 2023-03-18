check = 0
cost0 = 0
cost18 = 990
cost25 = 1390
ticket = int(input('Введите количество билетов, которое хотите приобрести: '))
age = [int(input('Введите возраст посетителя конференции: ')) for i in range(ticket)]
for a in age:
    if 0 <= a < 18:
        check += cost0
    if 18 <= a < 25:
        check += cost18
    elif 25 <= a < 125:
        check += cost25
    else:
        print('возраст указан неверно')
if ticket > 3:
    check -= check / 10
print(f'Сумма к оплате {int(check)} руб.')