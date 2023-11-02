def solution():
    total_earnings = 160  # Mike earned a total of $160
    hours_worked = 12  # Mike works 12 hours per week at his second job
    wage_per_hour = 9  # Mike earns $9 per hour at his second job

    # Calculate the earnings from Mike's second job
    earnings_second_job = hours_worked * wage_per_hour

    # Calculate the earnings from Mike's first job
    earnings_first_job = total_earnings - earnings_second_job
    result = earnings_first_job
    return result

print(solution())