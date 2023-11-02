def solution():
    # Calculate the yearly salary for Jame's new job and old job
    new_job_salary = 20 * 40 * 52  # $20 per hour, 40 hours per week, 52 weeks per year
    old_job_salary = 16 * 25 * 52  # $16 per hour, 25 hours per week, 52 weeks per year
    difference = new_job_salary - old_job_salary  # Calculate the difference between the two salaries
    result = difference
    return result

print(solution())