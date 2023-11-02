def solution():
    """Mrs. Thomson received an incentive worth $240. She spent 1/3 of the money on food and 1/5 of it on clothes. Then, she put in her savings account 3/4 of the remaining money. How much money did Mrs. Thomson save?"""
    incentive = 240

    # Calculate the amount spent on food
    food_spending = incentive / 3

    # Calculate the amount spent on clothes
    clothes_spending = incentive / 5

    # Calculate the total spending
    total_spending = food_spending + clothes_spending

    # Calculate the remaining amount
    remaining_amount = incentive - total_spending

    # Calculate the amount saved
    amount_saved = remaining_amount * (3/4)

    result = amount_saved
    return result

print(solution())