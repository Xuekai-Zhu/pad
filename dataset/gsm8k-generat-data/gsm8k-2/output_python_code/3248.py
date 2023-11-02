def solution():
    """A pound of strawberries costs $2.20 and a pound of cherries costs 6 times as much as strawberries. If Briget will buy 5 pounds of strawberries and 5 pounds of cherries, how much will it cost?"""
    strawberries_cost = 2.2
    cherries_cost = 6 * strawberries_cost
    total_cost = (5 * strawberries_cost) + (5 * cherries_cost)
    result = total_cost
    return result

print(solution())