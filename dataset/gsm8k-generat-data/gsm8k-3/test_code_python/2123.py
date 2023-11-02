def solution():
    """Bruce buys 5 packs of crayons at $5 each, 10 books at $5 each, and 3 calculators at $5 each. If he has $200, how many bags can he buy with the change if one costs $10 each?"""
    # Calculate the total cost of all the items
    total_cost = 5*5 + 10*5 + 3*5

    # Determine the amount of change Bruce has
    change = 200 - total_cost

    # Determine how many bags Bruce can buy with the change
    bag_cost = 10
    bags_can_buy = change // bag_cost

    # Display the number of bags Bruce can buy
    result = bags_can_buy
    return result

print(solution())