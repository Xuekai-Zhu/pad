def solution():
    """Farmer Brown fed 7 chickens and 5 sheep. How many total legs were there among the animals he fed?"""
    chickens_legs = 2
    sheep_legs = 4
    chickens_total = 7
    sheep_total = 5
    total_legs = (chickens_legs * chickens_total) + (sheep_legs * sheep_total)
    result = total_legs
    return result

print(solution())