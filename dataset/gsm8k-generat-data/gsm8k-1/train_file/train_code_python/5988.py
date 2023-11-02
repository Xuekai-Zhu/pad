def solution():
    """Sarah is buying Christmas presents for her family. She starts her shopping with a certain amount of money.
    She buys 2 toy cars for $11 each for her sons. She buys a scarf for $10 for her mother. Then she buys a beanie for $14 for her brother.
    If she has $7 remaining after purchasing the beanie, how much money did she start with?"""
    total_spent = 11*2 + 10 + 14 + 7
    initial_amount = total_spent
    return initial_amount

print(solution())