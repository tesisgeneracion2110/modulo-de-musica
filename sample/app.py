import music.song
import music.config
import os
import random
import secrets
from flask import Flask, jsonify, request, send_from_directory

UPLOAD_DIRECTORY = "files/"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)


def generate_structure():
    default_structures = [
        ["pre_chorus", 1],
        ["chorus", 1],
        ["verse", 1],
        ["outro", 1]
    ]
    structure = []

    i = random.randrange(1, 2)
    if i == 1:
        structure.append(["intro", 1])

    parts = random.randint(14, 24)
    for i in range(parts):
        structure.append(secrets.choice(default_structures))
    print(structure)
    return structure


def check_values(jsn):
    bpm = jsn['bpm'] if 'bpm' in jsn else None
    root = jsn['root'] if 'root' in jsn else None
    scale = jsn['scale'] if 'scale' in jsn else None
    n_chords = jsn['n_chords'] if 'n_chords' in jsn else None
    progression = jsn['progression'] if 'progression' in jsn else None
    n_beats = jsn['n_beats'] if 'n_beats' in jsn else None
    structure = jsn['structure'] if 'structure' in jsn else generate_structure()
    song = music.song.Song(bpm, root, scale, n_chords, progression, n_beats, structure)
    return song


@app.route("/music/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@app.route('/music', methods=['POST'])
def addProduct():
    song = check_values(request.json)
    response = music.config.prepare_song(song)
    print(response)
    return jsonify({"bpm": response[0],
                    "music": "music_" + str(response[1]) + ".wav",
                    "melody": "melody_" + str(response[1]) + ".mid"
                    })


if __name__ == '__main__':
    app.run(debug=True, port=4000)
