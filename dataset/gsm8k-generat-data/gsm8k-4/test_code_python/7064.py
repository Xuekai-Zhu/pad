def solution():
    """John can play 200 beats per minute. If he plays 2 hours a day for 3 days how many beats does he play?"""
    # Define the number of beats per minute and the total play time
    beats_per_minute = 200
    play_time = 2 * 60  # 2 hours in minutes

    # Calculate the total number of beats played over 3 days
    total_play_time = play_time * 3
    total_beats = total_play_time * beats_per_minute

    # return the result
    result = total_beats
    return result

print(solution())