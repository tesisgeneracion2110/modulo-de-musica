from FoxDot import *
import random
import music.chords
import music.start

Server.add_forward("localhost", 57120)


def check_parameters(song):
    if song.bpm is None:
        song.bpm = random.randrange(85, 96)
    if song.root is None:
        song.root = random.choice(['c', 'd', 'e', 'f', 'g', 'a', 'b'])
    if song.scale is None:
        song.scale = random.choice(['minor', 'major'])


def generate_chords_sounds(chords):
    ca = chords[0]
    cb = chords[1]
    cc = chords[2]
    cd = chords[3]

    cha = var([cd, ca, cb, cc], 4)
    chb = var([cd[0], ca[0], cb[0], cc[0]], 4)

    ch_sounds = [
        pluck(cha, dur=PDur(random.randrange(6), 8, random.randrange(3), random.choice([0.25, 0.5, 0.75])), amp=0.6),
        piano(cha, dur=PDur(random.randrange(6), 8, random.randrange(3), random.choice([0.25, 0.5, 0.75])), amp=0.7),
        blip(cha, dur=PDur(random.randrange(6), 8, random.randrange(3), random.choice([0.25, 0.5])), amp=0.8),
        zap(cha, dur=PDur(random.randrange(6), 8, random.randrange(3), random.choice([0.25, 0.5])), amp=2)
    ]

    ch_sounds2 = [
        pluck(cha, dur=PDur(random.randrange(6), 8, random.randrange(3), random.choice([0.25, 0.5, 0.75])), amp=0.6),
        piano(chb, dur=PDur(random.randrange(11), 16, random.randrange(3), random.choice([0.25, 0.5, 0.75])), amp=0.7),
        blip(chb, dur=PDur(random.randrange(11), 16, random.randrange(3), random.choice([0.25, 0.5, 0.75])), amp=0.8),
        zap(chb, dur=PDur(random.randrange(11), 16, random.randrange(3), random.choice([0.25, 0.5, 0.75])), amp=2)
    ]

    ci = random.randrange(len(ch_sounds))
    chord_sound = ch_sounds[ci]
    chord_sound2 = ch_sounds2[ci]

    return [chord_sound, chord_sound2]


def generate_other_sounds(chords):
    n_chords = len(chords)
    ca = chords[0]
    cb = chords[1]
    cc = chords[2]
    cd = chords[3]

    notes_bass = var([cd[0], ca[0], cb[0], cc[0]], 4)
    notes_aco = [ca[0], ca[1], ca[2], cb[0], cb[1], cb[2], cc[0], cc[1], cc[2], cd[0], cd[1], cd[2]]

    # Random bass
    dur_b = random.randrange(1, 6)

    bass_sounds = [
        bass(notes_bass, dur=PDur(dur_b, 16), amp=0.6)
    ]

    # Random accompanist 1
    notes_aco1 = PRand(notes_aco)[:n_chords * 2]
    dur = random.randrange(1, 6)

    aco_sounds = [
        charm(notes_aco1, dur=PDur(dur, 8), amp=0.8),
        prophet(notes_aco1, dur=PDur(dur, 8), amp=0.4),
        gong(notes_aco1, dur=PDur(dur, 8), amp=1.4)
    ]

    # Random accompanist 2
    notes_aco2 = PRand(notes_aco)[:8]
    aco_sounds2 = [
        """
        pads(notes_aco2, amp=[0.3, random.choice([0, 0.3]), random.choice([0, 0.3]), random.choice([0, 0.3])],
             output=2),
        viola(notes_aco2, amp=[0.7, random.choice([0, 0.7]), random.choice([0, 0.7]), random.choice([0, 0.7])],
              output=2),
        feel(notes_aco2, amp=[2.6, random.choice([0, 2.6]), random.choice([0, 2.6]), random.choice([0, 2.6])],
             output=2)
        """
    ]

    bi = random.randrange(len(bass_sounds))
    aai = random.randrange(len(aco_sounds))
    abi = random.randrange(len(aco_sounds2))

    bass_sound = bass_sounds[bi]
    aco_sound = aco_sounds[aai]
    aco_sound2 = aco_sounds2[abi]

    return [bass_sound, aco_sound, aco_sound2]


def generate_drums_sounds(n_beats):
    # Bass
    bas = ["x", "V", "X", "v"]
    bas_samples = [0, 0, 2, 0]
    bas_amp = [1.1, 0.7, 0.8, 1]

    # Drummer
    drum = ["o", "O", "i", "u", "I"]
    drum_samples = [0, 0, 2, 4, 1]
    drum_amp = [1.1, 0.4, 0.8, 1.2, 1.9]

    # Low Drummer
    l_drum = ["P", "R", "T", "g", "t"]
    l_drum_samples = [0, 0, 0, 2, 1]
    l_drum_amp = [1, 1, 1, 1, 1]

    # Random
    ib = random.randrange(4)
    ir = random.randrange(5)
    bom = bas[ib]
    sab = bas_samples[ib]
    amb = bas_amp[ib]
    red = drum[ir]
    sar = drum_samples[ir]
    amr = drum_amp[ir]
    print("Drums:", bom + " " + red)

    drums = [
        play(bom + "[ " + red + "]" + bom + red, sample=[sab, sar], amp=[amb, amr]),
        play(bom + "[-" + red + "]" + bom + red, sample=[sab, sar], amp=[amb, amr]),
    ]

    drums1 = [
        play("- [(-)]([--])"),
        play("- - - - "),
        play(" -  - - ")
    ]

    di = random.randrange(len(drums))
    dai = random.randrange(len(drums1))

    return [drums[di], drums1[dai]]


def prepare_song(song):
    # Check parameters
    check_parameters(song)
    print("SONG DETAILS")
    print("Bpm:", song.bpm)
    print("Root:", song.root)
    print("Scale:", song.scale)

    print("\nCHORDS")
    # Get chords and progression
    chords = music.chords.get_chords(song.n_chords, song.progression)
    print("Chords:", chords)

    # Get music sounds
    chords_sounds = generate_chords_sounds(chords)
    other_sounds = generate_other_sounds(chords)
    drums_sounds = generate_drums_sounds(song.n_beats)

    # Start music
    music.start.start_music(song, chords_sounds, other_sounds, drums_sounds)
