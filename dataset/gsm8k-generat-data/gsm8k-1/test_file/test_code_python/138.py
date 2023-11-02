def solution():
    """Jordan plays video games for 2 hours every day. He also has a part-time job where he earns $10 an hour. How much money would Jordan earn in one week if he spent his video game time working instead?"""
    gaming_hours_per_week = 2 * 7
    wage_per_hour = 10
    salary_per_week = (24 - gaming_hours_per_week) * wage_per_hour
    result = salary_per_week
    return result

print(solution())