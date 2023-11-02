def solution():
    """Borris liquor store uses 90 kilograms of grapes every 6 months. He is thinking of increasing his production by twenty percent. How many grapes does he need in a year after increasing his production?"""
    current_grape_usage = 90
    increased_percentage = 0.2
    new_grape_usage = current_grape_usage * (1 + increased_percentage)
    grapes_per_year = new_grape_usage * 2
    result = grapes_per_year
    return result

print(solution())