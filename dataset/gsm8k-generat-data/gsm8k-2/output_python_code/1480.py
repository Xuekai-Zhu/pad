def solution():
    """Mike watches TV for 4 hours every day. On the days he plays video games he plays for half as long as he watches TV. If he plays video games 3 days a week how long does he spend watching TV and playing video games?"""
    tv_time = 4 * 7  # 4 hours a day for 7 days
    game_time = (4/2) * 3  # Half as long as TV time for 3 days
    total_time = tv_time + game_time
    result = total_time
    return result

print(solution())