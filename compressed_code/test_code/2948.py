def solution():
    
    total_earned = 600
    clothes_spending = total_earned / 2
    remaining_money = total_earned - clothes_spending
    book_spending = remaining_money / 2
    money_left = remaining_money - book_spending
    result = money_left
    return result

print(solution())