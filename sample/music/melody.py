from FoxDot import *
from midiutil import MIDIFile

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


def voice_melody(song):
    notes = PRand(6)[:4].stutter(4)
    s_dur = PDur(PTri(random.randrange(1, 3), random.randrange(4, 6)), 8)
    print("\n\nMELODY")
    print("--Input--")
    print("Root:", song.root)
    print("Notes:", notes)
    print("Dur:", s_dur)

    # Start data processing
    index = [(index, row.index(song.root)) for index, row in enumerate(numbers) if song.root in row]
    root = numbers[index[0][0]][1]

    degrees = []

    for n in notes:
        degrees.append(root + major_scale[n])

    times = []
    durations = []
    n = 0
    i = 0

    while n < 16:
        times.append(n)
        durations.append(s_dur[i])
        n = n + s_dur[i]
        if i + 1 < len(s_dur):
            i += 1
        else:
            i = 0

    n = len(degrees)
    i = len(times)
    j = 0

    while n < i:
        degrees.append(degrees[j])
        j += 1
        n += 1

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
