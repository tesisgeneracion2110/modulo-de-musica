import music.song
import music.config

song = music.song.Song(
    None,
    "E",
    "major",
    4,
    None,
    2,
    [["intro", 1], ["pre_chorus", 1], ["chorus", 2]]
)

music.config.prepare_song(song)
