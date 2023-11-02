def solution():
    """Mrs. Thomson received an incentive worth $240. She spent 1/3 of the money on food and 1/5 of it on clothes. Then, she put in her savings account 3/4 of the remaining money. How much money did Mrs. Thomson save?"""
    incentive = 240
    food_spending = incentive / 3
    clothes_spending = incentive / 5
    remaining_money = incentive - food_spending - clothes_spending
    saved_money = remaining_money * (3/4)
    result = saved_money
    return result

print(solution())