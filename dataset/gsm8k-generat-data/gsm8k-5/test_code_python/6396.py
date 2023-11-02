def solution():
    diploma_pay = 4000  # Pay for a person holding a diploma certificate is $4000 per month
    degree_pay = diploma_pay * 3  # A person with a degree earns three times the amount paid to a diploma holder

    # Calculate Jared's annual pay after graduating with a degree
    jared_annual_pay = degree_pay * 12
    result = jared_annual_pay
    return result

print(solution())