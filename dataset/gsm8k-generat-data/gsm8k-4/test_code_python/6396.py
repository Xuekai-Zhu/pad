def solution():
    """For an operations manager job at a company, a person with a degree earns three times the amount paid to a diploma holder for the same position. How much will Jared earn from the company in a year after graduating with a degree if the pay for a person holding a diploma certificate is $4000 per month?"""
    # Define the monthly pay for a diploma holder
    diploma_pay = 4000

    # Calculate the annual pay for a diploma holder
    annual_diploma_pay = diploma_pay * 12

    # Calculate the annual pay for a degree holder
    degree_pay = diploma_pay * 3
    annual_degree_pay = degree_pay * 12

    # Calculate Jared's annual pay after graduating with a degree
    jared_annual_pay = annual_degree_pay

    result = jared_annual_pay
    return result

print(solution())