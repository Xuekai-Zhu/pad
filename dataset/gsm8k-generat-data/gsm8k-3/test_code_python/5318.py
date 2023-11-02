def solution():
    """Casey is going to stay at a motel while she works her summer job as a ski instructor. The hotel charges $280/week or $1000/month. If Casey will be staying 3 months, each with exactly 4 weeks, how much money does she save by paying monthly?"""
    # Define the cost of a weekly stay and a monthly stay
    WEEKLY_COST = 280
    MONTHLY_COST = 1000

    # Calculate the cost of staying for 3 months if paying weekly
    weekly_cost = WEEKLY_COST * 4 * 3

    # Calculate the cost of staying for 3 months if paying monthly
    monthly_cost = MONTHLY_COST * 3

    # Calculate the difference in cost between paying weekly and paying monthly
    cost_difference = weekly_cost - monthly_cost

    # Display the cost difference
    result = cost_difference
    return result

print(solution())