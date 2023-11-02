def solution():
    """Steve makes 40000$ a year as a teacher. He loses 20 percent to taxes, 10 percent to healthcare, and 800$ to local union dues. How much money does Steve take home?"""
    salary = 40000
    tax_percentage = 0.2
    healthcare_percentage = 0.1
    union_dues = 800
    remaining_salary = salary - (salary * tax_percentage) - (salary * healthcare_percentage) - union_dues
    result = remaining_salary
    return result

print(solution())