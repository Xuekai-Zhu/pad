def solution():
    
    initial_money = 204
    toy_cost = initial_money / 2
    remaining_money = initial_money - toy_cost
    book_cost = remaining_money / 2
    money_left = remaining_money - book_cost
    result = money_left
    return result

print(solution())