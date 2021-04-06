import random


def get_progression(number, pro):
    progression = []
    options = range(1, 8)
    if number is None:
        progression = [random.randrange(1, 8), random.randrange(1, 8), random.randrange(1, 8),
                       random.randrange(1, 8)]
    elif number == 2:
        if pro is None:
            values = random.sample(options, 2)
            progression = values + values
        else:
            progression = pro + pro
    elif number == 3:
        if pro is None:
            values = random.sample(options, 3)
            progression = values + [values[random.randrange(3)]]
        else:
            progression = pro + [pro[random.randrange(3)]]
    elif number == 4:
        if pro is None:
            values = random.sample(options, 4)
            progression = values
        else:
            progression = pro
    return progression


def get_chords(n_chords, pro):
    progression = get_progression(n_chords, pro)
    print('Progression:', progression)
    chords = []
    for x in range(len(progression)):
        available_chords = chords_list[progression[x] - 1]
        chords.append(random.choice(available_chords))
    return chords


# All chords list
chords_list = [
    [(0, 2, 4), (0, 2, -3)],
    [(1, 3, -2)],
    [(2, 4, -1), (2, 4, 6), (-5, -3, -1)],
    [(-4, -2, 0), (3, 5, 0)],
    [(-3, -1, 1), (4, 1, 6)],
    [(-2, 0, -5), (-2, 0, 2)],
    [(-1, 1, -4), (-1, 1, 3), (-1, -4, -6)]
]
