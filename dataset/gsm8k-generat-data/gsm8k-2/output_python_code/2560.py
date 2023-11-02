def solution():
    """Happy Island has 60 turtles. This means there are 10 more than 2 times as many turtles on Happy Island as on Lonely Island. How many turtles are there on Lonely Island?"""
    happy_island_turtles = 60
    lonely_island_turtles = (happy_island_turtles - 10) / 2
    result = lonely_island_turtles
    return result

print(solution())