def solution():
    """John can play 200 beats per minute. If he plays 2 hours a day for 3 days how many beats does he play?"""
    beats_per_minute = 200
    minutes_per_hour = 60
    hours_played = 2 * 3
    total_minutes_played = hours_played * minutes_per_hour
    total_beats_played = total_minutes_played * beats_per_minute
    result = total_beats_played
    return result

print(solution())