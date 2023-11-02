def solution():
    """Borris liquor store uses 90 kilograms of grapes every 6 months. He is thinking of increasing his production by twenty percent. How many grapes does he need in a year after increasing his production?"""
    # Define the initial grape usage per 6 months and the production increase percentage
    initial_grapes = 90
    production_increase = 0.2

    # Calculate the grape usage per 6 months after the production increase
    updated_grapes = initial_grapes * (1 + production_increase)

    # Calculate the grape usage per year after the production increase
    grapes_per_year = updated_grapes * 2

    result = grapes_per_year
    return result

print(solution())