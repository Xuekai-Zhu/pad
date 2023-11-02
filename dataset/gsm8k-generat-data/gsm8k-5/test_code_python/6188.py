def solution():
    # Calculate Dino's earnings from each job
    earnings_job1 = 20 * 10  # Dino works 20 hours at $10 per hour
    earnings_job2 = 30 * 20  # Dino works 30 hours at $20 per hour
    earnings_job3 = 5 * 40  # Dino works 5 hours at $40 per hour

    # Calculate Dino's total earnings
    total_earnings = earnings_job1 + earnings_job2 + earnings_job3

    # Calculate Dino's net income (earnings - expenses)
    net_income = total_earnings - 500

    result = net_income
    return result

print(solution())