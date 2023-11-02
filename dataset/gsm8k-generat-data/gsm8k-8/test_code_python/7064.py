def solution():
    # Define John's playing speed and time
    beats_per_minute = 200
    hours_per_day = 2
    days_played = 3

    # Calculate the total beats played
    total_beats_played = beats_per_minute * 60 * hours_per_day * days_played

    result = total_beats_played
    return result

print(solution())