def solution():
    starting_amount = 50
    daily_spending = 15
    current_savings = 0
    days_elapsed = 0

    while current_savings < 245:
        days_elapsed += 1
        current_savings = starting_amount - (days_elapsed * daily_spending)
    
    total_savings = current_savings * 2
    total_savings += 10
    total_savings += 245

    days_elapsed = (total_savings - starting_amount) // daily_spending
    result = days_elapsed
    return result

print(solution())