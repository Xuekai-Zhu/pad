def solution():
    """Jame gets a raise to $20 per hour and works 40 hours a week. His old job was $16 an hour for 25 hours per week. How much more money does he make per year in his new job than the old job if he works 52 weeks a year?"""
    new_job_pay = 20 * 40
    old_job_pay = 16 * 25
    difference = (new_job_pay - old_job_pay) * 52
    result = difference
    return result

print(solution())