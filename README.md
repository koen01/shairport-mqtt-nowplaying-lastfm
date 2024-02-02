# Now Playing Scrobbler

This Python script is designed to work as a Now Playing scrobbler, updating the currently playing track information on Last.fm based on the information received from MQTT topics. The script is intended to be used in environments where music playback information is available via MQTT (e.g., from Shairport-sync).

## Prerequisites

Make sure you have the following prerequisites set up:

- Python installed (version 3.x)
- Paho MQTT client library (`paho.mqtt.client`)
- PyLast library (`pylast`)
- MQTT broker with topics for artist, title, and album information

## Usage

### Environment Variables

Before running the script, set the necessary environment variables:

- `LASTFM_API_KEY`: Last.fm API key
- `LASTFM_API_SECRET`: Last.fm API secret
- `LASTFM_USERNAME`: Last.fm username
- `LASTFM_PASSWORD`: Last.fm password 
- `MQTT_BROKER`: MQTT broker address
- `MQTT_PORT`: MQTT broker port
- `MQTT_TOPIC`: MQTT topic for artist, title, and album information (i.e shairportsync/player/#)

### Running the Script

Run the script using the following command:

```bash
python nowplaying_script.py
