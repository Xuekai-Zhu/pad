def solution():
    """Jame gets a raise to $20 per hour and works 40 hours a week. His old job was $16 an hour for 25 hours per week. How much more money does he make per year in his new job than the old job if he works 52 weeks a year?"""
    # Calculate the annual salary of Jame's new job
    new_salary = 20 * 40 * 52

    # Calculate the annual salary of Jame's old job
    old_salary = 16 * 25 * 52

    # Calculate the difference in salary between the two jobs
    salary_difference = new_salary - old_salary

    # Display the difference in salary
    result = salary_difference
    return result

print(solution())