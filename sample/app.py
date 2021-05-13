import music.song
import music.config
import os
from flask import Flask, jsonify, request, send_from_directory

UPLOAD_DIRECTORY = "files/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)


@app.route("/music/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


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
                    "music": str(response[1]) + ".wav",
                    "melody": str(response[1]) + ".mid"
                    })


if __name__ == '__main__':
    app.run(debug=True, port=4000)
