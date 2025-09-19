# pogodi broj od 1 do 100
# racunalo "zamisli" jedan broj, a mi ga trebamo pogoditi
# racunalo nam daje hintove je li "zamisljeni" broj 
# manji ili veci od broja kojeg smo mi naveli

import random


counter = 0
secret_number = random.randint(1, 100)
# print(secret_number)


while True:
    users_number = int(input('Koji broj sam zamisio? '))
    counter += 1

    if users_number == secret_number:
        print(f'CESTITAMO!!! Pogodili ste broj iz {counter} puta')
        break
    else:
        if secret_number < users_number:
            print(f'Zamisljeni broj je manji od unesenog broja')
        else:
            print(f'Zamisljeni broj je veci od unesenog broja')
