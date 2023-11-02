def solution():
    
    initial_earnings = 600
    clothes_spending = initial_earnings / 2
    remaining_money = initial_earnings - clothes_spending
    book_spending = remaining_money / 2
    money_left = remaining_money - book_spending
    result = money_left
    return result

print(solution())