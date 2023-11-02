def solution():
    """Mia is buying Christmas gifts for her family. She has spent $30 on each of her 3 siblings, and the rest of her spending was for her parents. If Mia spent a total of $150 on Christmas gifts and each of her parents received gifts of equal value, how much money, in dollars, did she spend on each parent’s gift?"""
    total_spending = 150
    sibling_spending = 30 * 3
    parent_spending = total_spending - sibling_spending
    parent_gift_spending = parent_spending / 2
    result = parent_gift_spending
    return result

print(solution())