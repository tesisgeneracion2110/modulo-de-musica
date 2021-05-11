import music.song
import music.config
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/music', methods=['POST'])
def addProduct():
    song = music.song.Song(
        request.json['bpm'],
        request.json['root'],
        request.json['scale'],
        request.json['n_chords'],
        request.json['progression'],
        request.json['n_beats'],
        request.json['structure']
    )
    response = music.config.prepare_song(song)
    print(response)
    return jsonify({"bpm": response[0],
                    "music": "/home/oscar/Documents/records/music/" + str(response[1]) + ".wav",
                    "melody": "/home/oscar/Documents/records/melody/" + str(response[1]) + ".mid"
                    })


if __name__ == '__main__':
    app.run(debug=True, port=4000)
