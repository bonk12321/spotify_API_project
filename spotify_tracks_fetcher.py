import requests
import os
import base64
from dotenv import load_dotenv

load_dotenv()
def get_spotify_token():
    """Returns Spotify access token using Client Credentials Flow."""
    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise ValueError("Set SPOTIFY_CLIENT_ID and SPOTIFY_CLIENT_SECRET in .env")
    
    auth_str = f"{client_id}:{client_secret}"
    b64_auth_str = base64.b64encode(auth_str.encode()).decode()
    
    headers = {"Authorization": f"Basic {b64_auth_str}"}
    data = {"grant_type": "client_credentials"}
    
    response = requests.post("https://accounts.spotify.com/api/token", headers=headers, data=data)
    response.raise_for_status()
    token_json = response.json()
    return token_json["access_token"]

def get_headers():
    """Return the headers for Spotify API requests using the dynamic access token."""
    access_token = get_spotify_token()
    return {"Authorization": f"Bearer {access_token}"}

def get_artist_id(artist_name, headers):
    """Return the Spotify ID of an artist given their name."""
    search_url = "https://api.spotify.com/v1/search"
    params = {"q": artist_name, "type": "artist", "limit": 1}
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()
    
    if not data['artists']['items']:
        raise ValueError(f"Artist not found: {artist_name}")
    
    artist_id = data['artists']['items'][0]['id']
    print("Artist ID:", artist_id)
    return artist_id

def get_albums(artist_id, headers):
    """Return a list of all albums by the artist."""
    albums = []
    next_url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    
    while next_url:
        response = requests.get(next_url, headers=headers, params={"limit": 50})
        data = response.json()
        albums.extend(data['items'])
        next_url = data.get('next')
    
    return albums

def get_all_tracks(artist_id, albums, headers):
    """Return a list of all tracks by the artist from all their albums."""
    all_tracks = []
    
    for album in albums:
        album_id = album['id']
        next_tracks_url = f"https://api.spotify.com/v1/albums/{album_id}/tracks"
        
        while next_tracks_url:
            response = requests.get(next_tracks_url, headers=headers, params={"limit": 50})
            data = response.json()
            for track in data['items']:
                # Include only tracks where the artist is listed
                if any(artist['id'] == artist_id for artist in track['artists']):
                    all_tracks.append(track['name'])
            next_tracks_url = data.get('next')
    
    return all_tracks

if __name__ == "__main__":
    headers = get_headers()
    artist_name = "tygrysyn"  # replace with the artist you want to fetch
    
    artist_id = get_artist_id(artist_name, headers)
    albums = get_albums(artist_id, headers)
    print(f"Number of albums {artist_name} took part in: {len(albums)}")
    
    all_tracks = get_all_tracks(artist_id, albums, headers)
    print(f"Number of tracks {artist_name} took part in: {len(all_tracks)}")
    
    print(f"all  tracks {artist_name} took part in: ", all_tracks)
