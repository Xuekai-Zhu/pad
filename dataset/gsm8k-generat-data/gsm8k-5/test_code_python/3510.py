def solution():
    total_goal = 1000  # Alfred's total goal is to save $1,000 over 12 months
    starting_amount = 100  # Alfred has $100 left over from last year
    remaining_amount = total_goal - starting_amount  # Alfred needs to save this much more
    months = 12  # Alfred has 12 months to save

    # Calculate how much Alfred needs to save each month to meet his goal
    monthly_savings = remaining_amount / months
    result = monthly_savings
    return result

print(solution())