def solution():
    """Macey saves to buy herself a shirt that costs $3. She was able to save $1.50 already. How many weeks does she need to save for the remaining amount if she saves $0.50 per week?"""
    remaining_cost = 3 - 1.5
    savings_per_week = 0.5
    weeks_to_save = remaining_cost / savings_per_week
    result = weeks_to_save
    return result

print(solution())