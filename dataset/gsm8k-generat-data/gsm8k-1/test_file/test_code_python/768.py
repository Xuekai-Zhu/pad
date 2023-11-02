def solution():
    """Tatiana is deciding how much of her weekend she wants to spend playing soccer. She has 7 hours on Saturday and 5 hours on Sunday. She is dividing her time between soccer, video games, and reading. If she reads for 3 hours and plays video games for 1/3 of the remaining time, what percentage of her weekend does she spend playing soccer?"""
    saturday_hours = 7
    sunday_hours = 5
    reading_hours = 3
    remaining_time = (saturday_hours + sunday_hours) - reading_hours
    video_game_hours = remaining_time / 3
    soccer_hours = remaining_time - video_game_hours
    total_weekend_hours = saturday_hours + sunday_hours
    soccer_percentage = (soccer_hours / total_weekend_hours) * 100
    result = soccer_percentage
    return result

print(solution())