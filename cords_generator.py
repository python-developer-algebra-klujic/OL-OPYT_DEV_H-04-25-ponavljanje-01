tones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']


for index, tone in enumerate(tones):
    if index == len(tones) - 1:
        print(tone)
    else:
        print(tone, end=', ')
