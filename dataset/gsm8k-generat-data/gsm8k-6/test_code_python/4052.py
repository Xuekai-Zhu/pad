def solution():
    # Calculate Ernie's current income
    ernie_income = (4/5) * 6000
    
    # Calculate Jack's current income
    jack_income = 2 * (6000 * (1 - (4/5)))
    
    # Calculate the total combined income
    total_income = ernie_income + jack_income
    
    result = total_income
    return result

print(solution())