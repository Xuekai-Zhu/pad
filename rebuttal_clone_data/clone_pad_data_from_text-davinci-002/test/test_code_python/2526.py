def solution():
    initial_cost = 1300
    percent_needed = 40
    money_needed = initial_cost * (percent_needed / 100)
    additional_money = initial_cost - money_needed
    result = additional_money
    
    return result

print(solution())