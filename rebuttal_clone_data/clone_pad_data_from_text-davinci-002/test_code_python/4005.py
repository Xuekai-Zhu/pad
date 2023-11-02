def solution():
    initial_money = 20
    book_cost = 8
    poster_cost = 4
    money_left = initial_money - book_cost
    posters_bought = money_left / poster_cost
    result = posters_bought
    return result

print(solution())