def solution():
    """Kirt has a $6000 monthly salary when he started his job. After a year of working, his salary increased by 30%. How much are his total earnings after 3 years?"""
    start_salary = 6000
    year_1_salary = start_salary * 1.3
    year_2_salary = year_1_salary * 1.3
    year_3_salary = year_2_salary * 1.3
    total_earnings = (start_salary * 12) + (year_1_salary * 12) + (year_2_salary * 12) + (year_3_salary * 12)
    result = total_earnings
    return result

print(solution())