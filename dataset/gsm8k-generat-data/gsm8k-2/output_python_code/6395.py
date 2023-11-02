def solution():
    """For an operations manager job at a company, a person with a degree earns three times the amount paid to a diploma holder for the same position. How much will Jared earn from the company in a year after graduating with a degree if the pay for a person holding a diploma certificate is $4000 per month?"""
    diploma_salary = 4000 * 12 # annual salary for diploma holder
    degree_salary = 3 * diploma_salary # annual salary for degree holder
    result = degree_salary
    return result

print(solution())