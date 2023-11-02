def solution():
    current_investment = 90  # Jason's current investment is worth $90
    total_return = current_investment - (2 * 90)  # Jason has earned twice his investment in 5 months

    # Calculate the amount earned per month from the investment
    earning_per_month = total_return / 5
    result = earning_per_month
    return result

print(solution())