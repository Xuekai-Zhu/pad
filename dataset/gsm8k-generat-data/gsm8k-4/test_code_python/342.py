def solution():
    """In a 90-minute soccer game, Mark played 20 minutes, then rested after. He then played for another 35 minutes. How long was he on the sideline?"""
    # Define the total duration of the soccer game
    TOTAL_DURATION = 90

    # Define the durations of Mark's play and rest
    PLAY_DURATION_1 = 20
    REST_DURATION = TOTAL_DURATION - PLAY_DURATION_1
    PLAY_DURATION_2 = 35

    # Calculate the total duration of Mark's time on the sideline
    sideline_duration = REST_DURATION - PLAY_DURATION_2

    # return the result
    result = sideline_duration
    return result

print(solution())