def solution():
    """Roberto is raising chickens for eggs. He buys 4 chickens for $20 each. They cost $1 in total a week to feed and each produces 3 eggs a week that will last forever. He used to buy 1 dozen eggs a week and spent $2 per dozen. After how many weeks will the chickens be cheaper than buying his eggs?"""
    chicken_cost = 20 * 4
    weekly_feed_cost = 1 * 4
    weekly_egg_production = 3 * 4
    weekly_egg_cost = 2
    weeks = 0
    while (weekly_egg_cost * weeks) < (chicken_cost + (weekly_feed_cost * weeks)):
        weeks += 1
    result = weeks
    return result

print(solution())