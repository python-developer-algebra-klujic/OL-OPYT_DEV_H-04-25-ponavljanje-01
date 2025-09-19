# Generirati tablicu mnozenja do proizvoljnog broja

# do 10
# print('1, 2, 3, 4, 5, 6, 7, 8, 9, 10')
# print('2, 4, 6, 8, 10, 12, 14, 16, 18, 20')
#...

# # mnozenje s 1
# for number in range(10):
#     number_for_print = 1 * (number + 1)
#     if number_for_print < 10:
#         print('0', number_for_print, ' ', sep='', end=' ')
#     else:
#         print(number_for_print, ' ', sep='', end=' ')
# print()

# # mnozenje s 2
# for number in range(10):
#     number_for_print = 2 * (number + 1)
#     if number_for_print < 10:
#         print('0', number_for_print, ' ', sep='', end=' ')
#     else:
#         print(number_for_print, ' ', sep='', end=' ')
# print()

# # mnozenje s 3
# for number in range(10):
#     number_for_print = 3 * (number + 1)
#     if number_for_print < 10:
#         print('0', number_for_print, ' ', sep='', end=' ')
#     else:
#         print(number_for_print, ' ', sep='', end=' ')
# print()


# limit = int(input('Do kojeg broja zelite generirati tablicu mnozenja? '))

# for i in range(limit):
#     for j in range(limit):
#         number_for_print = (i + 1) * (j + 1)
#         # if number_for_print < 10:
#         #     # dodavanje 0 ispred broja -> bolja opcija koristenje str.zfill() metode
#         #     print('0', number_for_print, ' ', sep='', end=' ')
#         # else:
#         #     print(number_for_print, ' ', sep='', end=' ')

#         # text_to_print = f'{number_for_print:>5}'
#         # print(text_to_print, end='')
#         print(f'{number_for_print:>5}', end='')
#     print()


print()
print('Primjer koristenja str.zfill() metoda')
print()

number = 10
sub_total = 1999
tax = sub_total * 0.25
total = sub_total + tax

print(str(number).zfill(5))

# broj 1 prikazi tako da ukupno ima 5 brojki i ispred jedinice doda 4 nule
print(f'{str(1).zfill(5)}-1-2025')
# rezultat dijeljenja prikazi u celiji sirine 15 znakova, 
# poravnaj uz lijevi rub i zaokruzi na tri decimale
print(f'{13 / 7:<15.3f} EUR')

result = 13 / 7
print(type(result))
rounded_result = round(result, 3)
print(type(rounded_result))

print(f'{round(13 / 7, 3)} EUR')
