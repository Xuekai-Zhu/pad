def solution():
    
    starting_money = 21
    saved_money = 11
    comic_book_cost = 5
    puzzle_cost = 19
    total_spent = comic_book_cost + puzzle_cost
    money_left = starting_money - total_spent
    result = money_left
    return result

print(solution())