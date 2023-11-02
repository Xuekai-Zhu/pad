def solution():
    
    total_days = 4
    target_money = 100
    money_per_pound = 2
    
    
    monday_pounds = 8
    monday_money = monday_pounds * money_per_pound
    
    tuesday_pounds = monday_pounds * 3
    tuesday_money = tuesday_pounds * money_per_pound
    
    wednesday_money = 0  
    
    total_money = monday_money + tuesday_money + wednesday_money
    
    
    remaining_money = target_money - total_money
    
    
    pounds_needed = remaining_money / money_per_pound
    result = pounds_needed
    
    return result

print(solution())