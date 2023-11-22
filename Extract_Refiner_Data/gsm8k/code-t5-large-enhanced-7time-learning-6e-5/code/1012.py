def solution():
    
    initial_price = 120
    increase_percent = 5
    final_price = initial_price * (1 + increase_percent/100)
    result = final_price
    return result

print(solution())