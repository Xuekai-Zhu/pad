def solution():
    money_left = 51

    # Isabel bought a toy with half of the money, so she had half left
    remaining_money_1 = money_left * 2

    # Isabel bought a book for her brother with half of the remaining money, so she had half left
    remaining_money_2 = remaining_money_1 * 2

    # The remaining money at the end is half of what she had at first
    money_at_first = remaining_money_2 * 2
    result = money_at_first
    return result

print(solution())