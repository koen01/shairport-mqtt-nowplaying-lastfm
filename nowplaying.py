import paho.mqtt.client as mqtt
import pylast
import os

# Last.fm credentials
LASTFM_API_KEY = os.environ.get('LASTFM_API_KEY')
LASTFM_API_SECRET = os.environ.get('LASTFM_API_SECRET')
LASTFM_USERNAME = os.environ.get('LASTFM_USERNAME')
LASTFM_PASSWORD = LASTFM_PASSWORD = pylast.md5(os.environ.get('LASTFM_PASSWORD'))

# MQTT credentials
MQTT_BROKER = os.environ.get('MQTT_BROKER')
MQTT_PORT = int(os.environ.get('MQTT_PORT'))

# Shairport-sync MQTT topic
MQTT_TOPIC = os.environ.get('MQTT_TOPIC')

# Initialize global variables outside the function
current_artist = None
current_title = None
current_album = None

# Message callback function
def on_message(client, userdata, message):
    topic = message.topic
    payload = message.payload
    global current_artist
    global current_title
    global current_album

    if topic == "MQTT_TOPIC/artist":
        current_artist = payload
    elif topic == "MQTT_TOPIC/title":
        current_title = payload
    elif topic == "MQTT_TOPIC/album":
        current_album = payload
    else:
        return

    if current_artist is not None and current_title is not None and current_album is not None:

       # Update now playing to Last.fm
       try:
           lastfm.update_now_playing(artist=current_artist, title=current_title, album=current_album)
           print(f"{current_artist} - {current_title} - {current_album}")
           print("Now Playing updated successfully!")
           # Reset variables after processing
           current_artist = None
           current_title = None
           current_album = None
       except pylast.WSError as e:
           print("Error updating Now Playing:", e)


# Last.fm connection
lastfm = pylast.LastFMNetwork(api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET,
                               username=LASTFM_USERNAME, password_hash=LASTFM_PASSWORD)
# Mqtt connection
client = mqtt.Client()
client.on_message = on_message
client.connect(MQTT_BROKER, MQTT_PORT)
client.subscribe(MQTT_TOPIC)

# Start MQTT loop
client.loop_start()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
