def solution():
    """Movie tickets cost $5 each on a Monday, twice as much on a Wednesday, and five times as much as Monday on a Saturday. If Glenn goes to the movie theater on Wednesday and Saturday, how much does he spend?"""
    cost_monday = 5
    cost_wednesday = cost_monday * 2
    cost_saturday = cost_monday * 5
    glenns_cost = cost_wednesday + cost_saturday
    result = glenns_cost
    return result

print(solution())