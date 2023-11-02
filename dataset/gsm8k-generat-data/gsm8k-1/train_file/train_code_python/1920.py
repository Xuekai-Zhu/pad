def solution():
    """Lisa has 36 candies. On Mondays and Wednesdays, she eats 2 candies for each day and on the other days of the week she eats 1 candy for each day. How many weeks does it take for Lisa to eat all of the candies?"""
    total_candies = 36
    candies_eaten_on_mon_wed = 2 * 2  # 2 candies each on Monday and Wednesday
    candies_eaten_on_other_days = 5 * 1  # 1 candy each on other days
    candies_eaten_per_week = candies_eaten_on_mon_wed + candies_eaten_on_other_days
    weeks_to_finish_candies = total_candies // candies_eaten_per_week
    result = weeks_to_finish_candies
    return result

print(solution())