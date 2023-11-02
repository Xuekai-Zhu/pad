def solution():
    """A pound of strawberries costs $2.20 and a pound of cherries costs 6 times as much as strawberries.
    If Briget will buy 5 pounds of strawberries and 5 pounds of cherries, how much will it cost?"""
    # Define the cost of strawberries and cherries per pound
    strawberry_cost = 2.2
    cherry_cost = 6 * strawberry_cost

    # Calculate the total cost of 5 pounds of strawberries and 5 pounds of cherries
    total_cost = (5 * strawberry_cost) + (5 * cherry_cost)

    # return the result
    result = total_cost
    return result

print(solution())