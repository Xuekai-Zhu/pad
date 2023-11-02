def solution():
    
    borrowed_amount = 100
    increase_percentage = 10
    increase_amount = borrowed_amount * (increase_percentage / 100)
    total_amount = borrowed_amount + increase_amount
    result = total_amount
    return result

print(solution())