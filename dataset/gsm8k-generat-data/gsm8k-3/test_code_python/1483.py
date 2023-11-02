def solution():
    """Mia is buying Christmas gifts for her family. She has spent $30 on each of her 3 siblings, and the rest of her spending was for her parents. If Mia spent a total of $150 on Christmas gifts and each of her parents received gifts of equal value, how much money, in dollars, did she spend on each parent’s gift?"""
    # Calculate the total amount spent on gifts for siblings
    siblings_cost = 3 * 30

    # Calculate the amount spent on gifts for parents
    parent_cost = 150 - siblings_cost

    # Divide the parent cost by 2 to get the cost of each parent's gift
    parent_gift_cost = parent_cost / 2

    # Display the cost of each parent's gift
    result = parent_gift_cost
    return result

print(solution())