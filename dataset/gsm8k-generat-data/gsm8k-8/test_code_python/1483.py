def solution():
    # Calculate how much Mia spent on her siblings
    siblings_spending = 3 * 30

    # Calculate how much Mia spent on her parents
    parents_spending = 150 - siblings_spending

    # Divide parents' spending by 2 to get cost of each parent's gift
    parent_gift_cost = parents_spending / 2
    
    result = parent_gift_cost
    return result

print(solution())