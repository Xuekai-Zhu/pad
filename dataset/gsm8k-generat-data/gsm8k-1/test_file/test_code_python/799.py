def solution():
    """Kris is trying to earn a video game achievement for playing a total of 30 hours. If Kris plays for half an hour every day for 2 weeks then plays for 2 hours every day for a week, how many hours does she still need to play to earn the achievement?"""
    first_week_hours = 0.5 * 7 * 2
    second_week_hours = 2 * 7
    total_hours_played = first_week_hours + second_week_hours
    hours_left_to_play = 30 - total_hours_played
    result = hours_left_to_play
    return result

print(solution())