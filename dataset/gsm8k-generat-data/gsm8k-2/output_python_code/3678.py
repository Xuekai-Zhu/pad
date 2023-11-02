def solution():
    """Macey saves to buy herself a shirt that costs $3. She was able to save $1.50 already. How many weeks does she need to save for the remaining amount if she saves $0.50 per week?"""
    shirt_cost = 3
    saved_amount = 1.5
    remaining_amount = shirt_cost - saved_amount
    weekly_savings = 0.5
    weeks_needed = remaining_amount / weekly_savings
    result = weeks_needed
    return result

print(solution())