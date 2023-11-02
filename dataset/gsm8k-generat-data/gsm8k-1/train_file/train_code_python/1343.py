def solution():
    """Jame gets a raise to $20 per hour and works 40 hours a week. His old job was $16 an hour for 25 hours per week. How much more money does he make per year in his new job than the old job if he works 52 weeks a year?"""
    old_wage = 16
    old_hours = 25
    new_wage = 20
    new_hours = 40
    weeks_per_year = 52
    old_salary = old_wage * old_hours * weeks_per_year
    new_salary = new_wage * new_hours * weeks_per_year
    difference = new_salary - old_salary
    result = difference
    return result

print(solution())