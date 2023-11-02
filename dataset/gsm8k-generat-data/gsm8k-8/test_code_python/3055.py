def solution():
    # Define the initial amount of vinegar as 100%
    initial_vinegar = 100

    # Calculate the amount of vinegar left after the first year
    first_year_vinegar = initial_vinegar - (0.2 * initial_vinegar)

    # Calculate the amount of vinegar left after the second year
    second_year_vinegar = first_year_vinegar - (0.2 * first_year_vinegar)

    # Calculate the percent of vinegar left after 2 years
    percent_left = second_year_vinegar / initial_vinegar * 100
    result = percent_left
    return result

print(solution())