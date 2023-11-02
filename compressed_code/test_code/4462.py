def solution():
    
    total_spent = 9 + 11 + 30
    shoes_refund = 0.9 * 30
    total_spent -= shoes_refund
    money_left = 74 - total_spent
    result = money_left
    return result

print(solution())