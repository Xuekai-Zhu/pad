def solution():
    """A pound of strawberries costs $2.20 and a pound of cherries costs 6 times as much as strawberries. If Briget will buy 5 pounds of strawberries and 5 pounds of cherries, how much will it cost?"""
    strawberry_cost_per_lb = 2.20
    cherry_cost_per_lb = strawberry_cost_per_lb * 6
    total_cost = (strawberry_cost_per_lb * 5) + (cherry_cost_per_lb * 5)
    result = total_cost
    return result

print(solution())