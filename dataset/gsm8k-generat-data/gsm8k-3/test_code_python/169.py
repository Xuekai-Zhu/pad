def solution():
    """Borris liquor store uses 90 kilograms of grapes every 6 months. He is thinking of increasing his production by twenty percent. How many grapes does he need in a year after increasing his production?"""
    # Define the initial grape usage in 6 months and the percentage increase
    initial_grape_usage = 90
    percentage_increase = 0.2

    # Calculate the new grape usage in 6 months after the increase
    new_grape_usage = initial_grape_usage * (1 + percentage_increase)

    # Calculate the new grape usage in a year
    new_grape_usage_year = new_grape_usage * 2

    result = new_grape_usage_year
    return result

print(solution())