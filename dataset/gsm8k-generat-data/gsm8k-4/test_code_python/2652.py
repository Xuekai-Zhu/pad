def solution():
    """The school band is having a car wash to raise money. Their goal is to collect $150. So far they have earned $10 each from three families and $5 each from 15 families. How much more money do they have to earn to reach their goal?"""
    # Define the goal amount and the amount earned so far
    goal_amount = 150
    earned_amount = (10*3) + (5*15)

    # Calculate the amount they still need to earn
    remaining_amount = goal_amount - earned_amount

    # return the result
    result = remaining_amount
    return result

print(solution())