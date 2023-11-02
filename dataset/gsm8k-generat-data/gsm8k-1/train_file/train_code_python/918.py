def solution():
    """Aisha enjoys listening to music on her mp3 player. She starts with 500 songs on her mp3 player, then adds another 500 the week after that. She realizes her mp3 player has a large capacity for storing songs so she adds twice the amount she already had on her mp3 player. After a while, though, she decides that she doesn't like 50 of the songs and removes them. How many songs are on Aisha's mp3 player now?"""
    initial_songs = 500
    songs_added_week1 = 500
    songs_added_week2 = initial_songs * 2
    songs_removed = 50
    total_songs = initial_songs + songs_added_week1 + songs_added_week2 - songs_removed
    result = total_songs
    return result

print(solution())