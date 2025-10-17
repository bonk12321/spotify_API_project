# Spotify Artist Track Scraper

This Python project fetches all albums and tracks of a specific artist from Spotify using the Spotify API.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Environment Variables](#environment-variables)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/spotify_project.git
cd spotify_project
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the scraper:
```bash
python spotify_tracks.py
```

Example output:
```
Artist ID: 12345abcde
Number of albums: 12
Number of tracks: 123
['Track 1', 'Track 2', ...]
```

## Features

- Search for an artist by name.
- Retrieve all albums of the artist(also other artists if our artist made a feat with them).
- Retrieve all the artists tracks
- Automatically fetches Spotify access token using Client Credentials Flow.

## Environment Variables

Create a `.env` file in the project root with the following variables:
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```



