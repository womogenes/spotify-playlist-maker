# Spotify playlist maker

Create a playlist from a list of Spotify track URLs using the Spotify API.

## Get started

1. Install `spotipy` with

```
pip install spotipy
```

2. Go to https://developer.spotify.com and create a Spotify developer account if you don't already have one. Put the following into an `.env` file located at the project root:

```
SPOTIPY_CLIENT_ID=35efb03d...
SPOTIFY_CLIENT_SECRET=0f828700...
SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
```

3. Create a `tracks.txt` file with the URLs of the Spotify tracks you want to create a playlist of. An example is given in `tracks.txt.example`. Extraneous text will automatically be recognized with regex and removed.

4. Run `playlist_maker.py`.
