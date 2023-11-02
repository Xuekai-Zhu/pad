def solution():
    """Todd borrowed $100 from his brother to start a snow-cone stand. He has to repay him $110 as soon as he can. Todd spent $75 on ingredients for the snow cones. He sells 200 of them for $.75 each. After he pays back his brother, how much money does Todd have?"""
    # Define the initial loan and repayment amount
    loan_amount = 100
    repayment_amount = 110

    # Calculate the total revenue from selling snow cones
    snow_cone_revenue = 200 * 0.75

    # Calculate the total cost of the ingredients
    ingredient_cost = 75

    # Calculate the total profit
    total_profit = snow_cone_revenue - ingredient_cost - repayment_amount + loan_amount

    # Display the total profit
    result = total_profit
    return result

print(solution())