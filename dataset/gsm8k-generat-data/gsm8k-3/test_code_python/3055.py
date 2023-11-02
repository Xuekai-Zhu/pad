def solution():
    """Anthony keeps a bottle of vinegar in his cupboard for 2 years. Each year 20% of the vinegar evaporates. What percent of the vinegar is left after 2 years?"""
    # Define the initial amount of vinegar
    vinegar_amount = 100

    # Calculate the amount of vinegar left after the first year
    vinegar_amount = vinegar_amount * (1 - 0.2)

    # Calculate the amount of vinegar left after the second year
    vinegar_amount = vinegar_amount * (1 - 0.2)

    # Calculate the percentage of vinegar left
    vinegar_percent = vinegar_amount / 100 * 100

    # Display the percentage of vinegar left
    result = vinegar_percent
    return result

print(solution())