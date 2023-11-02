def solution():
    """Mia is buying Christmas gifts for her family. She has spent $30 on each of her 3 siblings, and the rest of her spending was for her parents. If Mia spent a total of $150 on Christmas gifts and each of her parents received gifts of equal value, how much money, in dollars, did she spend on each parent’s gift?"""
    # Define the amount spent on each sibling
    sibling_spending = 30

    # Calculate the total amount spent on siblings
    total_sibling_spending = sibling_spending * 3

    # Calculate the amount spent on parents
    parent_spending = 150 - total_sibling_spending

    # Calculate the amount spent on each parent's gift
    parent_gift = parent_spending / 2

    # return the result
    result = parent_gift
    return result

print(solution())