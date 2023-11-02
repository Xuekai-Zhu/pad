def solution():
    # Calculate the total cost for the cheap gym
    cheap_gym_cost = 12 * 10 + 50  # 12 months in a year

    # Calculate the cost of one month of the expensive gym
    expensive_gym_monthly_cost = 3 * 10  # 3 times more expensive than cheap gym

    # Calculate the sign-up fee for the expensive gym
    expensive_gym_signup_fee = 4 * expensive_gym_monthly_cost

    # Calculate the total cost for the expensive gym in the first year
    expensive_gym_cost = 12 * expensive_gym_monthly_cost + expensive_gym_signup_fee

    # Calculate the total cost for both gyms in the first year
    total_cost = cheap_gym_cost + expensive_gym_cost

    result = total_cost
    return result

print(solution())