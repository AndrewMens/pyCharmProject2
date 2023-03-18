per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму, которую планируете положить под проценты: '))
deposit = list(map(lambda x:float(x*money/100), per_cent.values()))
def f(deposit):
    for i in deposit:
        if i-int(i)==0:return int(i)

        else:return i
# deposit1 = list(map())
# [return int(i) if i-int(i)==0 else:return i for i in ]
print('deposit =', f(deposit))
# print('Максимальная сумма, которую вы можете заработать — ', max(f(deposit)))