def solution():
    """Farmer Brown fed 7 chickens and 5 sheep. How many total legs were there among the animals he fed?"""
    chicken_legs = 2
    sheep_legs = 4
    total_chickens = 7
    total_sheep = 5
    total_legs = (total_chickens * chicken_legs) + (total_sheep * sheep_legs)
    result = total_legs
    return result

print(solution())