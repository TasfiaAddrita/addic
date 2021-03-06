from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS

from spotify_model import Spotify
from youtube_model import YouTube

app = Flask(__name__)
CORS(app)

sp = Spotify()

@app.route('/')
def index():
    return "hello"

@app.route('/receivejson', methods=["POST"])
def get_json():
    js_request = request.get_json()
    if js_request['subject'] == 'spotify-connection':
        sp.spotify_auth()
        response = "connected to spotify"
        
    if js_request['subject'] == 'add-song':
        yt = YouTube(js_request['yt_url'])
        track = yt.get_artist_and_track()
        sp.set_track(track)
        # sp = Spotify(track)
        # sp.spotify_auth()

        if sp.get_track_id() != []:
            if sp.check_track_in_user_lib():
                response = "song already saved"
            else:
                sp.add_track()
                response = "song added"
        
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)