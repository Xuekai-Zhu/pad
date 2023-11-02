def solution():
    loan_amount = 100
    repayment_amount = 110
    ingredient_cost = 75
    number_of_snow_cones = 200
    price_per_snow_cone = 0.75
    total_revenue = number_of_snow_cones * price_per_snow_cone
    profit = total_revenue - ingredient_cost
    remaining_money = profit - repayment_amount
    result = remaining_money
    
    return result

print(solution())