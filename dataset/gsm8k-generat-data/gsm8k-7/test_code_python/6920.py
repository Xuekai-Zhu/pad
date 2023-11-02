def solution():
    principal = 5600
    interest_rate = 0.07
    num_years = 2

    # Calculate the amount of interest earned in the first year
    interest_year1 = principal * interest_rate

    # Calculate the total amount in the bank after the first year
    total_year1 = principal + interest_year1

    # Calculate the amount of interest earned in the second year
    interest_year2 = total_year1 * interest_rate

    # Calculate the total amount in the bank after the second year
    total_year2 = total_year1 + interest_year2
    result = total_year2
    return result

print(solution())