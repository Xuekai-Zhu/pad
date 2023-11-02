def solution():
    
    starting_money = 204
    toy_cost = starting_money // 2
    remaining_money = starting_money - toy_cost
    book_cost = remaining_money // 2
    money_left_over = remaining_money - book_cost
    result = money_left_over
    return result

print(solution())