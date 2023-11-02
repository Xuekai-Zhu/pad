def solution():
    
    books_needed = 8
    cost_per_book = 5
    money_on_hand = 13
    total_cost = books_needed * cost_per_book
    money_needed = total_cost - money_on_hand
    result = money_needed
    return result

print(solution())