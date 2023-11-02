def solution():
    num_seasons_per_year = 5
    num_days_per_year = 250
    num_seasons_stayed = 3

    # Calculate the total number of days spent on Orbius-5
    total_num_days = (num_days_per_year / num_seasons_per_year) * num_seasons_stayed
    result = total_num_days
    return result

print(solution())