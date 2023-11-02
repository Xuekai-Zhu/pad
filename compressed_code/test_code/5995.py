def solution():
    
    original_length = 30 
    reduction_percent = 30
    reduction_amount = original_length * (reduction_percent / 100)
    new_length = original_length - reduction_amount
    result = new_length
    return result

print(solution())