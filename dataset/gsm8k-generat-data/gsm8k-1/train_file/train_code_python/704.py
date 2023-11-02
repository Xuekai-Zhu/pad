def solution():
    """Isabel has some money in her piggy bank. She spent half the amount and bought a toy. She then spent half of the remaining money and bought her brother a book. If she has $51 left, how much money, in dollars, did she have at first?"""
    money_left = 51
    brother_book_cost = money_left * 2
    remaining_money = brother_book_cost
    toy_cost = remaining_money * 2
    initial_money = toy_cost
    result = initial_money
    return result

print(solution())