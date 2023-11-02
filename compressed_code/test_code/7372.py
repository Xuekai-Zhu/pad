def solution():
    
    initial_fee = 80
    yearly_increase = 10
    years_passed = 5 
    current_fee = initial_fee + (yearly_increase * years_passed)
    result = current_fee
    
    return result

print(solution())