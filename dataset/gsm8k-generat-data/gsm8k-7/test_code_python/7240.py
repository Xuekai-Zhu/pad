def solution():
    num_chickens = 4
    cost_per_chicken = 20
    weekly_feed_cost = 1
    eggs_per_chicken_per_week = 3
    eggs_per_dozen = 12
    egg_cost_per_dozen = 2

    # Calculate the total cost of buying the chickens
    total_chicken_cost = num_chickens * cost_per_chicken

    # Calculate how many eggs the chickens produce per week
    total_eggs_per_week = num_chickens * eggs_per_chicken_per_week

    # Calculate how many eggs Roberto needs to buy per week
    total_eggs_needed_per_week = eggs_per_dozen / 2

    # Calculate the cost of buying the necessary number of eggs per week
    total_egg_cost_per_week = total_eggs_needed_per_week * egg_cost_per_dozen / eggs_per_dozen

    # Calculate how many weeks it will take for the chickens to become cheaper than buying eggs
    weeks_to_break_even = total_chicken_cost / (total_eggs_per_week * 7 + weekly_feed_cost - total_egg_cost_per_week)

    result = weeks_to_break_even
    return result

print(solution())