def solution():
    """Mike has earned a total of $160 in wages this week. He received the wages for his first job, then later received the wages from his second job where he works 12 hours a week. If his second job pays $9 per hour then how much money, in dollars, did Mike receive from his first job?"""
    total_wages = 160
    second_job_pay = 9
    second_job_hours = 12
    second_job_wages = second_job_pay * second_job_hours
    first_job_wages = total_wages - second_job_wages
    result = first_job_wages
    return result

print(solution())