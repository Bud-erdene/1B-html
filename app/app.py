from flask import Flask, render_template
from .data import anime_list # Assuming data.py is in the same directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', animes=anime_list)

# Keep the hello_world route for now, or remove it if not needed for testing.
@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/anime/<int:anime_id>')
def anime_detail(anime_id):
    anime_to_display = None
    for anime in anime_list:
        if anime['id'] == anime_id:
            anime_to_display = anime
            break

    if anime_to_display:
        return render_template('anime_detail.html', anime=anime_to_display)
    else:
        return "Anime not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') # Added host='0.0.0.0' for broader accessibility if run in some environments
