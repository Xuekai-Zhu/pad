def solution():
    """Joan has 2 hours to get all her music practice done. She spends 30 minutes on the piano, 25 minutes writing music on her computer, and 38 minutes reading about the history of the piano. Her final work is to use a special finger exerciser. How much time does she have left to use this?"""
    total_time = 120 # in minutes
    time_on_piano = 30
    time_writing_music = 25
    time_reading_history = 38
    time_left = total_time - time_on_piano - time_writing_music - time_reading_history
    result = time_left
    return result

print(solution())