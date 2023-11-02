def solution():
    """Roberto is raising chickens for eggs. He buys 4 chickens for $20 each. They cost $1 in total a week to feed and each produces 3 eggs a week that will last forever. He used to buy 1 dozen eggs a week and spent $2 per dozen. After how many weeks will the chickens be cheaper than buying his eggs?"""
    chickens_cost = 4 * 20
    eggs_cost = 2
    chickens_feed_cost = 1 * 4
    chickens_eggs_per_week = 4 * 3
    eggs_per_week = 12
    weeks = 0
    while eggs_cost * eggs_per_week * weeks < chickens_cost + chickens_feed_cost * weeks:
        weeks += 1
    result = weeks
    return result

print(solution())