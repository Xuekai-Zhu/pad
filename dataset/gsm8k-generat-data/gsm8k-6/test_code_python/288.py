def solution():
    # Calculate the cost of the first gym membership for the first year
    cost_cheap_gym = 10*12 + 50  # $10 a month and $50 sign-up fee
    # Calculate the cost of the second gym membership for the first year
    cost_expensive_gym = (3*10)*4 + (3*10)  # 3 times more expensive and sign-up fee of 4 months membership

    # Calculate the total cost of gym membership for the first year
    total_cost = cost_cheap_gym + cost_expensive_gym
    result = total_cost
    return result

print(solution())