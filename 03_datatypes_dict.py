
'''
Exercise 3: Python datatypes - Dictionary

Goal 1: Creating a dictionary
    With your favorite song, create a dictionary with information such as:
    title, artist, album, genre, and years since release.
Goal 2: Extracting values
    With your dictionary, print the title and artist.
Goal 3: Adding new key-value pair
    Add a new key with years since release
    
'''

# Solution
song = {
    "title": "Kill this love",
    "artist": "Blackpink",
    "album": "Kill this love",
    "genre": "kpop",
    "releaseYear": 2019
}

print("title: ", song['title'], 'artist:', song['artist'])


song["yearsSinceRelease"] = 2022 - song['releaseYear']
print(song)