def solution():
    weekly_rate = 280  # The hotel charges $280/week
    monthly_rate = 1000  # The hotel also offers a monthly rate of $1000
    num_weeks = 12  # Casey will be staying for 3 months, each with 4 weeks

    # Calculate the total cost of staying at the hotel for 12 weeks using the weekly rate
    total_weekly_cost = weekly_rate * num_weeks

    # Calculate the total cost of staying at the hotel for 3 months using the monthly rate
    total_monthly_cost = monthly_rate * 3

    # Calculate the amount of money Casey saves by paying monthly
    savings = total_weekly_cost - total_monthly_cost
    result = savings
    return result

print(solution())