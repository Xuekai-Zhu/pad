def solution():
    """Todd borrowed $100 from his brother to start a snow-cone stand. He has to repay him $110 as soon as he can. Todd spent $75 on ingredients for the snow cones. He sells 200 of them for $.75 each. After he pays back his brother, how much money does Todd have?"""
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