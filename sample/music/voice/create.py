from midiutil import MIDIFile


def create_melody(melodies, tempo):
    tim = 0
    track = 0
    channel = 0
    volume = 100

    my_midi = MIDIFile(1)
    my_midi.addProgramChange(0, 0, 0, 0)
    my_midi.addTempo(track, tim, tempo)

    print("\n\nMELODY")

    for melody in melodies:
        print("Degrees:", melody.degrees)
        print("Durations:", melody.durations)
        print("Times:", melody.times, "\n")
        for i, pitch in enumerate(melody.degrees):
            my_midi.addNote(track, channel, pitch, melody.times[i], melody.durations[i], volume)

    with open("C:/Users/57300/Documents/BatchFoxDot/Recordings/major-scale.mid", "wb") as output_file:
        my_midi.writeFile(output_file)
