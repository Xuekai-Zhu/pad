def solution():
    """Todd borrowed $100 from his brother to start a snow-cone stand. He has to repay him $110 as soon as he can. Todd spent $75 on ingredients for the snow cones. He sells 200 of them for $.75 each. After he pays back his brother, how much money does Todd have?"""
    borrowed_amount = 100
    repayment_amount = 110
    ingredient_cost = 75
    snowcone_price = 0.75
    number_of_snowcones_sold = 200
    total_sales = number_of_snowcones_sold * snowcone_price
    net_income = total_sales - ingredient_cost
    money_left_after_repayment = net_income - (repayment_amount - borrowed_amount)
    result = money_left_after_repayment
    return result

print(solution())