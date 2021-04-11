from FoxDot import *
import time


def start_chords(chords):
    p1 >> chords[0]
    p2 >> chords[1]


def start_aco1(aco):
    p3 >> aco


def start_aco2(aco):
    p5 >> aco


def start_bass(bas):
    p4 >> bas


def start_drums(drums):
    d1 >> drums


def start_drums_aco(drums):
    d3 >> drums


def stop_bass():
    p4.stop()


def stop_aco1():
    p3.stop()


def stop_aco2():
    p5.stop()


def stop_drums():
    d1.stop()


def stop_drums_aco():
    d3.stop()


def intro(chords):
    start_chords(chords)
    stop_bass()
    stop_aco1()
    stop_aco2()
    stop_drums()
    stop_drums_aco()
    p6.stop()
    #Clock.future(16, prepare_stop)
    #Clock.future(32, stop)


def pre_chorus(chords, bas, drums):
    stop_aco2()
    start_chords(chords)
    start_bass(bas)
    p6 >> piano(PRand(6)[:4].stutter(4), dur=PDur(PRand(5)[:4], 8), oct=6, channel=2, output=2)
    if drums is not None:
        start_drums(drums)
    #Clock.future(16, prepare_stop)
    #Clock.future(32, stop)


def chorus(chords, bas, aco1, aco2, drums, melody):
    # p6 >> melody
    start_chords(chords)
    start_bass(bas)
    start_drums(drums[0])
    start_drums_aco(drums[1])
    start_aco1(aco1)
    start_aco2(aco2)


def verse(chords, aco2, drums):
    stop_aco1()
    stop_drums_aco()
    stop_bass()
    start_chords(chords)
    start_aco2(aco2)
    start_drums(drums)
    p6 >> piano(PRand(7)[:4].stutter(4), dur=PRand([0.25, 0.5, 1])[:8], oct=6, channel=2, output=2)


def outro(chords, melody):
    start_chords(chords)
    stop_bass()
    stop_aco1()
    stop_aco2()
    stop_drums()
    stop_drums_aco()
    # p6 >> melody
    #Clock.future(16, prepare_stop)
    #Clock.future(32, stop)


def start_music(song, chords, others, drums, chorus_melody):
    Clock.bpm = song.bpm
    Scale.default.set(song.scale)
    Root.default.set(song.root)

    parts = song.structure

    print("\n\nSTRUCTURE")
    tim = 0
    for part in parts:
        if part[0] == "intro":
            print("intro:", tim)
            Clock.future(tim + 3, intro, kwargs={
                "chords": chords
            })
        elif part[0] == "pre_chorus":
            print("pre_chorus:", tim)
            Clock.future(tim + 3, pre_chorus, kwargs={
                "chords": chords,
                "bas": others[0],
                "drums": drums[2]
            })
        elif part[0] == "chorus":
            print("chorus:", tim)
            Clock.future(tim + 3, chorus, kwargs={
                "chords": chords,
                "bas": others[0],
                "aco1": others[1],
                "aco2": others[2],
                "drums": drums,
                "melody": chorus_melody
            })
        elif part[0] == "verse":
            print("verse:", tim)
            Clock.future(tim + 3, verse, kwargs={
                "chords": chords,
                "aco2": others[2],
                "drums": drums[3]
            })
        elif part[0] == "outro":
            print("outro:", tim)
            Clock.future(tim + 3, outro, kwargs={
                "chords": chords,
                "melody": chorus_melody
            })
        tim = tim + (part[1] * 16)

    print("end:", tim)
    song_time = tim * 60 / song.bpm
    print("Time:", song_time)
    time.sleep(song_time + 2)
    p8 >> donk()
    time.sleep(4)
    Clock.clear()
    exit()

    Go()
