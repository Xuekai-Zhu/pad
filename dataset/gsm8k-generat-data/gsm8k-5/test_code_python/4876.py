def solution():
    # Calculate MegaCorp's total revenue for the year
    daily_revenue = (3000000 + 5000000) - 30000000  # MegaCorp earns $3,000,000 from mining, $5,000,000 from oil refining, and spends $30,000,000 on expenses per day
    yearly_revenue = daily_revenue * 365  # Assuming 365 days in a year

    # Calculate the 1% fine
    fine = yearly_revenue * 0.01
    result = fine
    return result

print(solution())