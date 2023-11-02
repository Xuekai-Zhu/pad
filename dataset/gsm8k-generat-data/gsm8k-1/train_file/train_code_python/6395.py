def solution():
    """For an operations manager job at a company, a person with a degree earns three times the amount paid to a diploma holder for the same position. How much will Jared earn from the company in a year after graduating with a degree if the pay for a person holding a diploma certificate is $4000 per month?"""
    diploma_pay = 4000
    degree_pay = 3 * diploma_pay
    annual_pay = 12 * degree_pay
    result = annual_pay
    return result

print(solution())