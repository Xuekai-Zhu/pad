def solution():
    total_candies = 36
    candy_per_mon_wed = 2 * 2  # Two candies each on Monday and Wednesday
    candy_per_other_days = 5 * 1  # One candy each on the other days
    total_candies_eaten_per_week = candy_per_mon_wed + candy_per_other_days

    # Calculate the number of weeks needed to eat all the candies
    num_weeks = total_candies // total_candies_eaten_per_week
    if total_candies % total_candies_eaten_per_week != 0:
        num_weeks += 1
    result = num_weeks
    return result

print(solution())