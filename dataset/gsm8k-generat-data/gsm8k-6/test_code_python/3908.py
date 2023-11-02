def solution():
    # Calculate the total number of times Michael cleans himself in 52 weeks
    bath_times = 2 * 52  # Michael takes a bath twice a week
    shower_times = 1 * 52  # Michael takes a shower once a week
    total_cleaning_times = bath_times + shower_times
    result = total_cleaning_times
    return result

print(solution())