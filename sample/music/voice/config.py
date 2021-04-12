from FoxDot import *
import secrets
import random
import music.voice.melody
import music.voice.create

numbers = [
        ["C", 60],
        ["D", 62],
        ["E", 64],
        ["F", 65],
        ["G", 55],
        ["A", 57],
        ["B", 59]
    ]

major_scale = [0, 2, 4, 5, 7, 9, 11]
minor_scale = [0, 2, 3, 5, 7, 8, 10]

crp = random.SystemRandom()


def get_degrees(song, notes):
    index = [(index, row.index(song.root)) for index, row in enumerate(numbers) if song.root in row]
    root = numbers[index[0][0]][1]
    f_degrees = []
    for note in notes:
        if song.scale == "major":
            f_degrees.append(root + major_scale[note])
        else:
            f_degrees.append(root + minor_scale[note])
    return f_degrees


def generate_melody(song, notes, s_dur, t):
    f_degrees = get_degrees(song, notes)

    times = []
    durations = []
    degrees = []

    for dur in s_dur:
        durations.append(dur)

    durations *= 2

    i = t
    for dur in durations:
        times.append(i)
        i += dur

    i = t + 4
    j = 0
    for tim in times:
        if tim < i:
            degrees.append(f_degrees[j])
        else:
            j += 1
            degrees.append(f_degrees[j])
            i += 4

    chorus = music.voice.melody.Melody(degrees, durations, times)
    return chorus


def create_melody(song):
    melodies = []

    # Chorus data
    chorus_notes = crp.sample(range(1, 7), 4)
    chorus_dur = PDur(PRand(5)[:4], 8)

    parts = song.structure
    tim = 0

    for part in parts:
        if part[0] == "pre_chorus":
            chorus = crp.sample(range(1, 7), 4)
            dur = PDur(PRand(1, 5)[:4], 8)
            melody = generate_melody(song, chorus, dur, tim)
            melodies.append(melody)
        elif part[0] == "chorus" or part[0] == "outro":
            melody = generate_melody(song, chorus_notes, chorus_dur, tim)
            melodies.append(melody)
        elif part[0] == "verse":
            chorus = crp.sample(range(1, 7), 4)
            dur = PDur(PRand(2, 6)[:4], 8)
            melody = generate_melody(song, chorus, dur, tim)
            melodies.append(melody)
        tim += (part[1] * 16)

    music.voice.create.create_melody(melodies, song.bpm)
