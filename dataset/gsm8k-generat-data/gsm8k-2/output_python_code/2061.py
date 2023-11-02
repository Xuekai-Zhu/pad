def solution():
    """Joan has 2 hours to get all her music practice done. She spends 30 minutes on the piano, 25 minutes writing music on her computer, and 38 minutes reading about the history of the piano. Her final work is to use a special finger exerciser. How much time does she have left to use this?"""
    total_practice_time = 2 * 60
    piano_time = 30
    computer_time = 25
    history_time = 38
    used_time = piano_time + computer_time + history_time
    remaining_time = total_practice_time - used_time
    result = remaining_time
    return result

print(solution())