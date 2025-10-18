import unittest
import pytest
from unittest.mock import patch
from spotify_tracks_fetcher import get_artist_id

## MOCKOWANIE Z UNITTEST ##
# class TestSpotifyFunctions(unittest.TestCase):

#     test_cases = [
#         #test no.1 - artist existent
#         {
#             "input_artist": "AnyArtist",
#             "mock_json": {'artists' : {'items': [{'id': '12345'}]}},
#             "expected": '12345',
#             "raises": None
#         },
#         #test no.2 - artist nonexistent
#         {
#             "input_artist": "NoArtist",
#             "mock_json": {'artists': {'items':[]}},
#             "expected": None,
#             "raises": ValueError
#         },
#         #test no.3 - no 'artists' slot in response
#         {
#             "input_artist": "BrokenAPI",
#             "mock_json": {},
#             "expected": None,
#             "raises": KeyError
#         }
#     ]

#     @patch('spotify_tracks_fetcher.requests.get')
#     def test_get_artist_id_various(self,mock_get):
#         for case in self.test_cases:
#             mock_get.return_value.json.return_value = case["mock_json"]
#             if case["raises"]:
#                 with self.assertRaises(case["raises"]):
#                     get_artist_id(case["input_artist"], headers={})
#             else:
#                 result = get_artist_id(case["input_artist"],headers={})
#                 self.assertEqual(result, case["expected"])

# if __name__ == '__main__':
#     unittest.main()

## MOCKOWANIE PYTEST ##
@pytest.mark.parametrize("mock_json, expected, raises", [
    ({"artists": {"items": [{"id": "12345"}]}}, "12345", None),
    ({"artists": {"items": []}},None, ValueError),
    ({}, None, KeyError)
])

@patch("spotify_tracks_fetcher.requests.get")
def test_get_artist_id(mock_get, mock_json, expected, raises):
    mock_get.return_value.json.return_value = mock_json

    if raises:
        with pytest.raises(raises):
            get_artist_id("AnyArtist",headers={})
    else:
        result = get_artist_id("AnyArtist",headers={})
        assert result == expected