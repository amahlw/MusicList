from Song import Song


class Playlist:
    def __init__(self):
        self.__first_song = None

    # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

    def add_song(self, title):
        new_song = Song(title)
        next.song = self.__first_song

    # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

    def find_song(self, title):
        song_count = 0
        current_song = self.__first_song

        # assited by chegg tutor
        while current_song != None:
            if current_song.get_title() == title:
                song_count += 1
                return song_count

            if current_song.get_title() != title:
                song_count += 1
                current_song = current_song.next

    # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed.

    def remove_song(self, title):

        last_song = self.__first_song
        current_song = self.__first_song

        if current_song.get_title() == title:
            self.__first_song = self.__first_song.get_next_song()
            return f"Erased {current_song.get_title()} from the playlist."

        while current_song.get_title() != title:
            last_song = current_song
            current_song = current_song.get_next_song()

            if current_song == None:
                return f"Not available."

    # TODO: Create a method called length, which returns the number of songs in the playlist.

    def length(self):
        song_count = 0
        current_song = self.__first_song

        while current_song != None:
            song_count += 1
            current_song = current_song.get_next_song()

        return song_count

    # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

    # Example:
    # 1. Song Title 1
    # 2. Song Title 2
    # 3. Song Title 3

    def print_songs(self):
        current_song = self.__first_song

        while current_song != None
        print(current_song)
        current_song = current_song.next
