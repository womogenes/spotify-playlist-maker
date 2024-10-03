import re
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load environment variables
load_dotenv()

# Set up Spotify API credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIFY_REDIRECT_URI")

# Initialize Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               scope="playlist-modify-private"))

def extract_spotify_urls(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    
    # Regex pattern for Spotify track URLs
    pattern = r"https://open\.spotify\.com/track/([a-zA-Z0-9]+)(?:\?si=[a-zA-Z0-9]+)?"
    
    # Find all matches
    spotify_urls = re.findall(pattern, content)
    return spotify_urls

def create_playlist(track_urls):
    # Create a new private playlist
    user_id = sp.me()["id"]
    playlist = sp.user_playlist_create(user_id, input("Name of playlist: "), public=True)
    
    # Add tracks to the playlist
    track_ids = [url.split("/")[-1].split("?")[0] for url in track_urls]
    sp.playlist_add_items(playlist["id"], track_ids)
    
    return playlist["external_urls"]["spotify"]

def main():
    file_path = "./tracks.txt"  # Replace with your file path
    track_urls = extract_spotify_urls(file_path)
    
    if track_urls:
        playlist_url = create_playlist(track_urls)
        print(f"Playlist created successfully! You can find it here: {playlist_url}")
    else:
        print("No Spotify track URLs found in the file.")

if __name__ == "__main__":
    main()
