def solution():
    
    current_speed = 10
    current_bill = 20
    new_speed1 = 20
    new_bill1 = current_bill + 10
    new_speed2 = 30
    new_bill2 = current_bill * 2
    yearly_savings = (new_bill2 - new_bill1) * 12
    result = yearly_savings
    return result

print(solution())