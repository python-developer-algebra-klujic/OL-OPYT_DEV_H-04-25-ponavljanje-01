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


limit = int(input('Do kojeg broja zelite generirati tablicu mnozenja? '))

for i in range(limit):
    for j in range(limit):
        number_for_print = (i + 1) * (j + 1)
        # if number_for_print < 10:
        #     print('0', number_for_print, ' ', sep='', end=' ')
        # else:
        #     print(number_for_print, ' ', sep='', end=' ')

        # text_to_print = f'{number_for_print:>5}'
        # print(text_to_print, end='')
        print(f'{number_for_print:>5}', end='')
    print()
