def solution():
    """Jake is watching a new show, and is worried about how much time he has spent watching it. He spent half the day on Monday watching his show, 4 hours on Tuesday watching his show, a quarter of the day on Wednesday watching his show, and he spent half as much time watching the show on Thursday as he had done in total throughout the previous few days. On Friday, he finally finished watching it. If the entire show is 52 hours long, how many hours did Jake watch on Friday?"""
    total_hours = 52
    monday_hours = 0.5 * 24
    tuesday_hours = 4
    wednesday_hours = 0.25 * 24
    previous_hours = monday_hours + tuesday_hours + wednesday_hours
    thursday_hours = previous_hours / 2
    hours_watched = previous_hours + thursday_hours
    friday_hours = total_hours - hours_watched
    result = friday_hours
    return result

print(solution())