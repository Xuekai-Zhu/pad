def solution():
    """Verna loves to eat fruit. She bought three apples at $1.50 each, five oranges at $0.80 each, and six peaches at $0.75 each. If she gave $20, how much change did she receive?"""
    apples_bought = 3
    oranges_bought = 5
    peaches_bought = 6
    apple_cost = 1.5
    orange_cost = 0.8
    peach_cost = 0.75
    total_cost = (apples_bought * apple_cost) + (oranges_bought * orange_cost) + (peaches_bought * peach_cost)
    change = 20 - total_cost
    result = change
    return result

print(solution())