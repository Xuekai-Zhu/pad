def solution():
    total_days_in_year = 365
    total_seinfeld_episodes = 180
    if total_seinfeld_episodes >= total_days_in_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())