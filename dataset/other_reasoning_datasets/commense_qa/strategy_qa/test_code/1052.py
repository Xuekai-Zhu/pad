def solution():
    total_days_leap_year = 366
    total_days_restless = 467.5
    total_days_watched = total_days_restless * num_episodes
    if total_days_watched > total_days_leap_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())