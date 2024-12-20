import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# import seaborn as sns
from dotenv import load_dotenv

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('CLIENT_SECRET')
garrix_uri = 'https://open.spotify.com/artist/60d24wfXkVzDSfLS6hyCjZ'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
result = spotify.artist_top_tracks(garrix_uri)

pront(result)

# data = []
# if response.status_code > 199 and response.status_code < 300:
#     data = response.text
# else:
#     print(f'API connection malfunction. Response {response.status_code}')


# load the .env file variables
load_dotenv()
