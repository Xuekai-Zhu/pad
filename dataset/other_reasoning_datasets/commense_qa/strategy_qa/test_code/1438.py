def solution():
    # Define the average retail CEO's salary and the average retail associate's hourly wage range
    retail_CEO_salary = 14000000
    retail_associate_wage_range = (8, 13)
    # Convert the hourly wage range to an annual salary range using 2000 working hours per year
    retail_associate_salary_range = (retail_associate_wage_range[0] * 2000, retail_associate_wage_range[1] * 2000)
    # Check if the CEO's salary is greater than the highest retail associate salary
    if retail_CEO_salary > retail_associate_salary_range[1]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())