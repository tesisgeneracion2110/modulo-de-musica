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

    # degrees = [60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number

    # times = [0, 1, 2, 2.75, 3.5, 4, 4.5, 5, 5.5, 6, 6.75, 7.5, 8, 9, 10, 10.75]
    # times = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    tim = 0  # In beats
    track = 0
    channel = 0
    # duration = 1  # In beats
    tempo = song.bpm  # In BPM
    volume = 100  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created automatically)
    MyMIDI.addProgramChange(0, 0, 0, 0)
    MyMIDI.addTempo(track, tim, tempo)

    for i, pitch in enumerate(degrees):
        MyMIDI.addNote(track, channel, pitch, times[i], durations[i], volume)

    with open("C:/Users/57300/Documents/BatchFoxDot/Recordings/major-scale.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)

    # chorus_melody = piano(notes, dur=s_dur, output=2)
