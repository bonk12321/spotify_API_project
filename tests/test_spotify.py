import pytest
from spotify_tracks_fetcher import get_albums, get_all_tracks, get_artist_id, get_headers

ARTIST_NAME = "Tygrysyn"

@pytest.fixture
def headers():
    """Return headers for Spotify API requests"""
    return get_headers()

@pytest.fixture
def artist_id(headers):
    """Returns spotify ID fot a sample artist"""
    return get_artist_id(ARTIST_NAME, headers)

@pytest.fixture
def albums(artist_id, headers):
    """Return list of albums for the sample artist"""
    return get_albums(artist_id, headers)

def test_artist_id(headers):
    artist_id = get_artist_id(ARTIST_NAME, headers)
    assert isinstance(artist_id, str)
    assert len(artist_id) > 0

def test_get_albums(headers, artist_id):
    albums_list = get_albums(artist_id, headers)
    assert isinstance(albums_list, list)
    assert len(albums_list) > 0

def test_get_all_tracks(headers, artist_id, albums):
    tracks = get_all_tracks(artist_id, albums, headers)
    assert isinstance(tracks, list)
    assert len(tracks) > 0