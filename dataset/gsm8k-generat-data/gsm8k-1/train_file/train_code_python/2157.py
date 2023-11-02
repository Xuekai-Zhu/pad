def solution():
    """A housewife goes to the market. She spent 2/3 of her $150. How much does she have left?"""
    initial_money = 150
    spent_money = initial_money * (2/3)
    left_money = initial_money - spent_money
    result = left_money
    return result

print(solution())