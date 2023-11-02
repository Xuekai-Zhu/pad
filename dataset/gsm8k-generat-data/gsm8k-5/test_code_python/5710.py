def solution():
    total_spending = 5000  # Peter needs $5,000 to cover all the spending for the travel
    current_savings = 2900  # Peter has $2,900 in savings right now
    monthly_savings = 700  # Peter can save up $700 each month

    # Calculate the remaining amount Peter needs to save
    remaining_savings = total_spending - current_savings

    # Calculate the number of months needed to reach the remaining savings goal
    months_needed = remaining_savings / monthly_savings
    result = months_needed
    return result

print(solution())