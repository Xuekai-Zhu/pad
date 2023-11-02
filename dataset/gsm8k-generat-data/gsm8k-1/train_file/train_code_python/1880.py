def solution():
    """A bird eats 7 berries a day. Samuel has 5 birds. How many berries do Samuel's birds eat in 4 days?"""
    berries_per_bird_per_day = 7
    num_birds = 5
    num_days = 4
    total_beries = berries_per_bird_per_day * num_birds * num_days
    result = total_beries
    return result

print(solution())