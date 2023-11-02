def solution():
    # Calculate the total salary in the old job
    salary_old = 16 * 25 * 52  # $16 per hour, 25 hours per week, 52 weeks per year

    # Calculate the total salary in the new job
    salary_new = 20 * 40 * 52  # $20 per hour, 40 hours per week, 52 weeks per year

    # Calculate the difference in salary between the two jobs
    difference = salary_new - salary_old
    result = difference
    return result

print(solution())