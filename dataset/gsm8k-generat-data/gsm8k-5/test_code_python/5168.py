def solution():
    initial_money = 204  # Isabel has $204 in her piggy bank
    spent_money = initial_money / 2  # Isabel spends half of the initial money
    remaining_money = initial_money - spent_money  # Isabel has half of the initial money left
    spent_money_second = remaining_money / 2  # Isabel spends half of the remaining money on a book for her brother
    remaining_money_second = remaining_money - spent_money_second  # Isabel has the remaining money after buying the book

    result = remaining_money_second
    return result

print(solution())