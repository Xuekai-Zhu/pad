def solution():
    """Todd borrowed $100 from his brother to start a snow-cone stand. He has to repay him $110 as soon as he can. Todd spent $75 on ingredients for the snow cones. He sells 200 of them for $.75 each. After he pays back his brother, how much money does Todd have?"""
    # Define the initial amount borrowed and the repayment amount
    initial_borrowing = 100
    repayment_amount = 110

    # Define the ingredient cost and the sales price per snow cone
    ingredient_cost = 75
    snowcone_price = 0.75

    # Calculate the total revenue from selling snow cones
    total_revenue = 200 * snowcone_price

    # Calculate the total profit after all expenses and repayment
    total_profit = total_revenue - ingredient_cost - repayment_amount + initial_borrowing

    result = total_profit
    return result

print(solution())