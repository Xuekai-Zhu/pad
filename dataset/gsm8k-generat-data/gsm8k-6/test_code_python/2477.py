def solution():
    # Calculate the amount earned from the second job
    second_job_hours = 12  # hours worked at the second job
    second_job_pay = 9  # pay per hour at the second job
    second_job_earnings = second_job_hours * second_job_pay  # total earnings from the second job

    # Calculate the amount earned from the first job
    total_earnings = 160  # total earnings for the week
    first_job_earnings = total_earnings - second_job_earnings  # earnings from the first job

    result = first_job_earnings
    return result

print(solution())