def solution():
    """Isabel has $204 in her piggy bank. She spent half the amount and bought a toy. 
    She then spent half of the remaining money and bought her brother a book. 
    How much money, in dollars, was left over?"""
    starting_money = 204
    toy_cost = starting_money // 2
    remaining_money = starting_money - toy_cost
    book_cost = remaining_money // 2
    money_left_over = remaining_money - book_cost
    result = money_left_over
    return result

print(solution())