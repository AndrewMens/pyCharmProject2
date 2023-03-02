check = 0
ticket = int(input('Введите количество билетов, которое хотите приобрести: '))
age = [int(input('Введите количество лет посетителя конференции: ')) for i in range(ticket)]
for a in age:
    if 18 <= a < 25:
        check += 990
    if a >= 25:
        check += 1390
if ticket > 3:
    check -= check / 10
print(f'Сумма к оплате {int(check)} руб.')