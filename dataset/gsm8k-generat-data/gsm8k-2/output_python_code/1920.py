def solution():
    """Lisa has 36 candies. On Mondays and Wednesdays, she eats 2 candies for each day and on the other days of the week she eats 1 candy for each day. How many weeks does it take for Lisa to eat all of the candies?"""
    candy_count = 36
    monday_wednesday_candies = 2 * 2
    rest_of_week_candies = 5 * 1
    candies_per_week = monday_wednesday_candies + rest_of_week_candies
    weeks_to_finish = candy_count / candies_per_week
    result = weeks_to_finish
    return result

print(solution())