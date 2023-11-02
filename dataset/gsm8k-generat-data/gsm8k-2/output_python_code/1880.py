def solution():
    """A bird eats 7 berries a day. Samuel has 5 birds. How many berries do Samuel's birds eat in 4 days?"""
    berries_per_bird_per_day = 7
    total_birds = 5
    days = 4
    total_beries = berries_per_bird_per_day * total_birds * days
    result = total_beries
    return result

print(solution())