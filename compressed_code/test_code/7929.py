def solution():
    
    initial_value = 4000
    percent_reduction = 30
    reduction_amount = initial_value * (percent_reduction / 100)
    current_value = initial_value - reduction_amount
    result = current_value
    return result

print(solution())