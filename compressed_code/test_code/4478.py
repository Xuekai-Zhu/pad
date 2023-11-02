def solution():
    
    borrowed_money = 100
    repayment_amount = 110
    ingredient_cost = 75
    snow_cones_sold = 200
    snow_cone_price = 0.75

    revenue = snow_cones_sold * snow_cone_price
    profit = revenue - ingredient_cost
    remaining_money = profit - repayment_amount + borrowed_money
    result = remaining_money
    return result

print(solution())