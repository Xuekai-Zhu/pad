def solution():
    
    initial_amount = 100
    percent_increase = 10
    increase_amount = initial_amount * (percent_increase / 100)
    total_amount = initial_amount + increase_amount
    result = total_amount
    return result

print(solution())