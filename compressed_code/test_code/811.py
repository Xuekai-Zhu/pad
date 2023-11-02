def solution():
    
    dimes_value = 0.1
    quarters_value = 0.25
    nickels_value = 0.05
    initial_money = (4 * dimes_value) + (4 * quarters_value) + (7 * nickels_value)
    additional_money = 5 * quarters_value
    total_money = initial_money + additional_money
    result = total_money
    return result

print(solution())