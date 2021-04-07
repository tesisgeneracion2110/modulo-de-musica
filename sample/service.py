import music.song
import music.config

song = music.song.Song(
    None,
    None,
    None,
    None,
    None,
    None,
    [
        ["intro", 1],
        ["pre_chorus", 1],
        ["chorus", 1],
        ["verse", 1],
        ["outro", 1]
    ]
)

music.config.prepare_song(song)
