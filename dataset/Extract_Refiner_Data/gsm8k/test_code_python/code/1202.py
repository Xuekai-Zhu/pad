def solution():
    
    house_value = 250000
    loan_value = house_value * 0.4
    debt_cost = loan_value * 0.6
    leftover_money = loan_value - debt_cost
    result = leftover_money
    return result

print(solution())