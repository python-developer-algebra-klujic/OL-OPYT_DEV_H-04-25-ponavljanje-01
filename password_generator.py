'''
mala velika slova, brojevi, posebni znakovi
DULJINA PASSWORDA
    minimalni broj znakova = 8 - ostaviti korisniku da definira
    zeljeni broj znakova
    max broj znakova
random
graaficki prikaz jakosti passorda / definiraiti razine
'''

# import modula
import random


# definicija ulaznih/pocetnih vrijednosti
password = ''
min_password_lenght = 35

# posebni znakovi - od 33 - 47 i 58 - 64 i 91 - 96 i 123 - 126
# brojevi - od 48 - 57
# velika slova - 65 - 90
# mala slova - 97 - 122


# generiranje passworda
for _ in range(min_password_lenght):
    ascii_broj = random.randint(33, 126)
    letter = chr(ascii_broj)
    password = password + letter



# ispis
print()
print(f'Generirani password je: {password}')
print()
