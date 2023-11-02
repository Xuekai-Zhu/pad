def solution():
    # Calculate the total time it will take the 3 men to complete all 5 jobs
    total_time = 3 * 5  # 3 men, 5 jobs

    # Calculate the total amount of money earned by each man
    total_money = total_time * 10  # $10 per hour

    # Calculate the total amount earned by all three men
    total_earnings = total_money * 3  # 3 men

    result = total_earnings
    return result

print(solution())