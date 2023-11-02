def solution():
    """Isabel has $204 in her piggy bank. She spent half the amount and bought a toy. She then spent half of the remaining money and bought her brother a book. How much money, in dollars, was left over?"""
    initial_money = 204
    toy_cost = initial_money / 2
    remaining_money = initial_money - toy_cost
    book_cost = remaining_money / 2
    money_left = remaining_money - book_cost
    result = money_left
    return result

print(solution())