def solution():
    """John had $20. He spent 1/5 of his money on snacks and 3/4 of the remaining money on necessities. How much is left of John's money?"""
    initial_money = 20
    snacks_cost = initial_money / 5
    remaining_money = initial_money - snacks_cost
    necessities_cost = remaining_money * 3 / 4
    money_left = remaining_money - necessities_cost
    result = money_left
    return result

print(solution())