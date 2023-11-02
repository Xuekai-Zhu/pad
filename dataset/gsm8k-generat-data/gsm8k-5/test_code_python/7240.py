def solution():
    num_chickens = 4  # Roberto buys 4 chickens
    cost_per_chicken = 20  # Each chicken costs $20
    weekly_feed_cost = 1  # It costs $1 in total to feed the chickens per week
    eggs_per_chicken_per_week = 3  # Each chicken produces 3 eggs per week
    eggs_per_dozen = 12  # There are 12 eggs in a dozen
    egg_cost_per_dozen = 2  # Roberto used to buy 1 dozen eggs per week for $2

    # Calculate the cost of keeping the chickens per week
    weekly_chicken_cost = (num_chickens * cost_per_chicken) + weekly_feed_cost

    # Calculate the cost of buying eggs per week
    weekly_egg_cost = egg_cost_per_dozen / eggs_per_dozen

    # Calculate the number of weeks it will take for the chickens to be cheaper than buying eggs
    num_weeks = (num_chickens * eggs_per_chicken_per_week) / (weekly_chicken_cost - weekly_egg_cost)

    result = num_weeks
    return result

print(solution())