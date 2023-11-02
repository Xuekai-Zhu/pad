def solution():
    # Define Kem's hourly wage
    kem_wage = 4

    # Calculate Shem's hourly wage
    shem_wage = 2.5 * kem_wage

    # Calculate Shem's daily wage
    shem_daily_wage = shem_wage * 8

    # Round the answer to two decimal places
    result = round(shem_daily_wage, 2)
    return result

print(solution())