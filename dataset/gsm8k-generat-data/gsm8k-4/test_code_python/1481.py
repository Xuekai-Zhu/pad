def solution():
    """Mike watches TV for 4 hours every day. On the days he plays video games he plays for half as long as he watches TV. If he plays video games 3 days a week how long does he spend watching TV and playing video games?"""
    # Define the number of hours Mike watches TV each day
    tv_hours_per_day = 4

    # Calculate the number of hours Mike plays video games on each day he plays
    games_hours_per_day = tv_hours_per_day / 2

    # Calculate the total hours Mike spends watching TV and playing video games each week
    total_hours_per_week = (tv_hours_per_day * 7) + (games_hours_per_day * 3)

    # return the result
    result = total_hours_per_week
    return result

print(solution())