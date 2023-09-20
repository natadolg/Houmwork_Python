s = input('Введите фразу стихотворения: ')
list_s = s.split()
glasn = 'аяиюоуе'
count_glasn = []
for x in list_s:
    n = 0
    for y in x:
        if y in glasn:
            n += 1
    count_glasn.append(n)

# print(list_s)
# print(count_glasn)

k = 'Парам пам-пам'
for i in range(len(count_glasn) - 1):
    if count_glasn[i] != count_glasn[i + 1]:
        k = 'Пам парам'
        break
print(k)

## К сожалению, не могу придумать, как/на каком этапе в данной программе использовать функции высшего порядка.
##Прошу вас, Станислав, подсказать.
##Заранее благодарю.
