def solution():
    """Martha gets prize points every time she shops at her local grocery store. She gets 50 points per $10 spent, plus a 250 point bonus if she spends more than $100. Martha buys 3 pounds of beef for $11 each, 8 pounds of fruits and vegetables for $4/pound, 3 jars of spices for $6 each, and other groceries totaling $37. How many points does Martha get?"""
    # Calculate the total spent on groceries
    total_spent = 3 * 11 + 8 * 4 + 3 * 6 + 37

    # Calculate the bonus points
    if total_spent > 100:
        bonus_points = 250
    else:
        bonus_points = 0

    # Calculate the prize points
    prize_points = total_spent // 10 * 50

    # Calculate the total points
    total_points = bonus_points + prize_points

    result = total_points
    return result

print(solution())