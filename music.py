import spotify
import threading

logged_in_event = threading.Event()
def connection_state_listener(session):
	if session.connection.state is spotify.ConnectionState.LOGGED_IN:
		logged_in_event.set()

session = spotify.Session()
loop = spotify.EventLoop(session)
loop.start()
session.on(spotify.SessionEvent.CONNECTION_STATE_UPDATED, connection_state_listener)

lines = [line.rstrip('\n') for line in open('auth.txt')]
# Get username and password

print session.connection.state
session.login(lines[0], lines[1])
print session.connection.state

logged_in_event.wait()

print session.connection.state

# Log in

print len(session.playlist_container)
# Print number of playlists

container = session.playlist_container
print container.is_loaded
container.load()

print container.is_loaded


print container[0].load().name
track = session.get_track('spotify:track:2Foc5Q5nqNiosCNqttzHof')
print track.load().name

container[0].add_tracks(track)
container.load()
 # Adds Get Lucky to first playlist, called SendCailinMusic
loop.stop()