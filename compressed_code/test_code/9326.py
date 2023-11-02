def solution():
    
    
    first_year_allowance = 50 * 52
    second_year_wage = 9 * 30 * 52
    total_savings = first_year_allowance + second_year_wage
    total_spending = 35 * 104
    car_cost = 15000
    money_left = total_savings - total_spending
    money_needed = car_cost - money_left
    result = money_needed
    return result

print(solution())