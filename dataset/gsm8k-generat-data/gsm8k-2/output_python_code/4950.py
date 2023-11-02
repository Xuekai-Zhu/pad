def solution():
    """If Joe spent 1/9 of his pocket money of $450 on chocolates and 2/5 on fruits, how much money does he have left?"""
    pocket_money = 450
    chocolates_spending = pocket_money * (1/9)
    fruits_spending = pocket_money * (2/5)
    total_spending = chocolates_spending + fruits_spending
    remaining_money = pocket_money - total_spending
    result = remaining_money
    return result

print(solution())