def solution():
    # Calculate the total cost of buying the chickens
    chicken_cost = 4 * 20

    # Calculate the eggs cost per week before buying the chickens
    former_eggs_cost_per_week = 2

    # Calculate the eggs cost per egg before buying the chickens
    former_eggs_cost_per_egg = former_eggs_cost_per_week / (12 * 3)

    # Calculate the cost of feeding the chickens per week
    chicken_feed_cost_per_week = 4 * 1

    # Calculate the number of eggs produced per week by the chickens
    chicken_eggs_produced_per_week = 4 * 3

    # Calculate the eggs cost per egg after buying the chickens
    chicken_eggs_cost_per_egg = chicken_feed_cost_per_week / chicken_eggs_produced_per_week

    # Calculate after how many weeks the chickens will be cheaper than buying eggs
    weeks_until_cheaper = chicken_cost / (former_eggs_cost_per_egg - chicken_eggs_cost_per_egg)
    result = weeks_until_cheaper
    return result

print(solution())