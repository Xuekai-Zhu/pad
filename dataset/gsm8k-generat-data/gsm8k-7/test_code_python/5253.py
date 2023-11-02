def solution():
    initial_pay = 10.0
    first_year_raise = 0.20
    second_year_cut = 0.25

    # Calculate Cary's pay after the first year
    first_year_pay = initial_pay * (1 + first_year_raise)

    # Calculate Cary's pay after the second year
    second_year_pay = first_year_pay * (1 - second_year_cut)

    result = second_year_pay
    return result

print(solution())