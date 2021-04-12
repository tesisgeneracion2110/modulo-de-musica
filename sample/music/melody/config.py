from FoxDot import *
from midiutil import MIDIFile
import secrets
import random

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


def voice_melody(song):
    notes = crp.sample(range(1, 7), 4)
    s_dur = PDur(PRand(5)[:4], 8)
    print("\n\nMELODY")
    print("--Input--")
    print("Root:", song.root)
    print("Scale:", song.scale)
    print("Notes:", notes)
    print("Dur:", s_dur)

    # Start data processing
    index = [(index, row.index(song.root)) for index, row in enumerate(numbers) if song.root in row]
    root = numbers[index[0][0]][1]

    f_degrees = []

    for note in notes:
        if song.scale == "major":
            f_degrees.append(root + major_scale[note])
        else:
            f_degrees.append(root + minor_scale[note])

    times = []
    durations = []

    for dur in s_dur:
        durations.append(dur)

    durations *= 2

    i = 0
    for dur in durations:
        times.append(i)
        i += dur

    print("Degrees:", f_degrees)

    i = 4
    j = 0
    degrees = []

    for tim in times:
        if tim < i:
            degrees.append(f_degrees[j])
        else:
            j += 1
            degrees.append(f_degrees[j])
            i += 4

    print("\n--Output--")
    print("Root:", root)
    print("Degrees:", degrees)
    print("Durations:", durations)
    print("Times:", times)

    tim = 0
    track = 0
    channel = 0
    tempo = song.bpm
    volume = 100

    my_midi = MIDIFile(1)
    my_midi.addProgramChange(0, 0, 0, 0)
    my_midi.addTempo(track, tim, tempo)

    for i, pitch in enumerate(degrees):
        my_midi.addNote(track, channel, pitch, times[i], durations[i], volume)

    with open("C:/Users/57300/Documents/BatchFoxDot/Recordings/major-scale.mid", "wb") as output_file:
        my_midi.writeFile(output_file)

    # chorus_melody = piano(notes, dur=s_dur, output=2)
