def solution():
    """Mike has earned a total of $160 in wages this week. He received the wages for his first job, then later received the wages from his second job where he works 12 hours a week. If his second job pays $9 per hour then how much money, in dollars, did Mike receive from his first job?"""
    total_wages = 160
    hours_worked_second_job = 12
    wage_per_hour_second_job = 9
    total_wages_second_job = hours_worked_second_job * wage_per_hour_second_job
    wages_from_first_job = total_wages - total_wages_second_job
    result = wages_from_first_job
    return result

print(solution())