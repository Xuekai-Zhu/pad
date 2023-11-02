def solution():
    # Calculate the total amount spent on Mia's siblings
    siblings_spending = 30 * 3

    # Calculate the amount of money Mia spent on her parents
    mia_parents_spending = 150 - siblings_spending

    # Calculate the amount of money Mia spent on each parent's gift
    parent_gift_spending = mia_parents_spending / 2

    result = parent_gift_spending
    return result

print(solution())