def solution():
    """Bruce buys 5 packs of crayons at $5 each, 10 books at $5 each, and 3 calculators at $5 each. If he has $200, how many bags can he buy with the change if one costs $10 each?"""
    # Calculate the total cost of the items Bruce bought
    total_cost = (5 * 5) + (10 * 5) + (3 * 5)

    # Calculate the amount of change Bruce has
    change = 200 - total_cost

    # Calculate the number of bags Bruce can buy with the change
    num_bags = change // 10

    # Return the result
    result = num_bags
    return result

print(solution())