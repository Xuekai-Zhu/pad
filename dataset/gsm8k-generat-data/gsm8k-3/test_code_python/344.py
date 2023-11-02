def solution():
    """In a 90-minute soccer game, Mark played 20 minutes, then rested after. He then played for another 35 minutes. How long was he on the sideline?"""
    # Define the length of the soccer game and the time Mark played
    GAME_LENGTH = 90
    MARK_PLAYED_1 = 20
    MARK_PLAYED_2 = 35

    # Calculate the total time Mark was on the sideline
    sideline_time = GAME_LENGTH - (MARK_PLAYED_1 + MARK_PLAYED_2)

    # Display the sideline time
    result = sideline_time
    return result

print(solution())