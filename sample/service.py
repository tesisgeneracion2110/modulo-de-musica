import music.song
import music.config

song = music.song.Song(
    None,
    None,
    None,
    None,
    None,
    2,
    [["intro", 1], ["pre_chorus", 1], ["chorus", 2]]
)

music.config.prepare_song(song)
