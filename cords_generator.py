tones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

print()
for index, tone in enumerate(tones):
    if index == len(tones) - 1:
        print(index + 1, tone)
    else:
        print(index + 1, tone, end=', ')

print()
users_tone = input('Upisite ton iz liste za koji zelite generirati akord: ')

# dur 0, 4, 7
# mol 0, 3, 7

index_users_tone = tones.index(users_tone.upper())

# Nacin uporabom % operatora
# first_tone = tones[index_users_tone]
# dur_middle_tome = tones[((index_users_tone + 4) % 12)]
# mol_middle_tome = tones[((index_users_tone + 3) % 12)]
# last_tone = tones[((index_users_tone + 7) % 12)]

# Nacin uporabom .extend() metode
# tones.extend(tones)
# first_tone = tones[index_users_tone]
# dur_middle_tome = tones[index_users_tone + 4]
# mol_middle_tome = tones[index_users_tone + 3]
# last_tone = tones[index_users_tone + 7]

# Nacin oduzimanjem duzine liste od indeksa selektiranog tona
first_tone = tones[index_users_tone]
dur_middle_tome = tones[(index_users_tone + 4) - len(tones)]
mol_middle_tome = tones[(index_users_tone + 3) - len(tones)]
last_tone = tones[(index_users_tone + 7) - len(tones)]

dur_message = f'{users_tone.upper()} ({first_tone}, {dur_middle_tome}, {last_tone})'
mol_message = f'{users_tone.upper()} ({first_tone}, {mol_middle_tome}, {last_tone})'

print()
print(dur_message)
print(mol_message)
print()
