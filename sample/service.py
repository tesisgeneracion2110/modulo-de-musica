import music.song
import music.config

song = music.song.Song(
    None,
    None,
    None,
    3,
    None,
    None,
    [
        ["intro", 2],
        ["pre_chorus", 2],
        ["chorus", 2],
        ["verse", 2],
        ["chorus", 2],
        ["verse", 2],
        ["pre_chorus", 2],
        ["chorus", 2],
        ["outro", 1]
    ]
)

music.config.prepare_song(song)
