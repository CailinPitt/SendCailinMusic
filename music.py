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

artist = raw_input('Enter an artist: ')

search = session.search(artist)
search.loaded_event.wait()
# Search for artist

print container[0].load().name
track1 = search.tracks[0]
track2 = search.tracks[1]
print track1.load().name
print track2.load().name

container[0].add_tracks(track1)
# container[0].add_tracks(track2)
container[0].load()
 # Adds first song that is returned from search to first playlist, called SendCailinMusic
session.logout()
loop.stop()
