def solution():
    first_day_cans = 20
    increase_per_day = 5
    num_days = 5

    # Calculate the total number of cans collected after 5 days
    total_cans = first_day_cans + (increase_per_day * (num_days - 1))

    # Calculate the weekly goal by dividing the total number of cans by the number of days they collect
    weekly_goal = total_cans / num_days
    result = weekly_goal
    return result

print(solution())