def solution():
    loan = 100  # Todd borrowed $100 from his brother
    repayment = 110  # Todd has to repay his brother $110
    expenses = 75  # Todd spent $75 on ingredients for the snow cones
    revenue = 200 * 0.75  # Todd sells 200 snow cones for $0.75 each

    # Calculate Todd's profit after expenses and loan repayment
    profit = revenue - expenses - repayment + loan

    result = profit
    return result

print(solution())