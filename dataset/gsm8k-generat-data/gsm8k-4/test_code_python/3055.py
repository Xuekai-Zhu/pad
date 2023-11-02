def solution():
    """Anthony keeps a bottle of vinegar in his cupboard for 2 years. Each year 20% of the vinegar evaporates. What percent of the vinegar is left after 2 years?"""
    # Define the initial amount of vinegar
    initial_vinegar = 100

    # Calculate the amount of vinegar left after the first year
    vinegar_after_first_year = initial_vinegar * 0.8

    # Calculate the amount of vinegar left after the second year
    vinegar_after_second_year = vinegar_after_first_year * 0.8

    # Calculate the percentage of vinegar left after 2 years
    vinegar_percentage = vinegar_after_second_year / initial_vinegar * 100

    # Return the result
    result = vinegar_percentage
    return result

print(solution())