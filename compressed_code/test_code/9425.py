def solution():
    
    borrowed_money = 20 + 40 + 30
    gifted_money = 70
    savings = 100
    total_money = borrowed_money + gifted_money + savings
    spent_money = total_money * (3/4)
    remaining_money = total_money - spent_money
    result = remaining_money
    return result

print(solution())