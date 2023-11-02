def solution():
    """Casey is going to stay at a motel while she works her summer job as a ski instructor. The hotel charges $280/week or $1000/month. If Casey will be staying 3 months, each with exactly 4 weeks, how much money does she save by paying monthly?"""
    # Define the weekly and monthly rates
    weekly_rate = 280
    monthly_rate = 1000

    # Calculate the cost of staying for 3 months using weekly rates
    weekly_cost = 3 * 4 * weekly_rate

    # Calculate the cost of staying for 3 months using monthly rates
    monthly_cost = 3 * monthly_rate

    # Calculate the difference in cost between paying weekly and paying monthly
    savings = weekly_cost - monthly_cost

    result = savings
    return result

print(solution())