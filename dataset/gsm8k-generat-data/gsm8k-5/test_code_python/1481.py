def solution():
    tv_hours = 4  # Mike watches TV for 4 hours every day
    game_days = 3  # Mike plays video games 3 days a week
    game_hours = tv_hours / 2  # Mike plays video games for half as long as he watches TV

    # Calculate the total hours Mike spends watching TV and playing video games in a week
    total_hours = (tv_hours * 7) + (game_hours * game_days)
    result = total_hours
    return result

print(solution())