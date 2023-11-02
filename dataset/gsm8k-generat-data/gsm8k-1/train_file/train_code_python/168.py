def solution():
    """Borris liquor store uses 90 kilograms of grapes every 6 months. He is thinking of increasing his production by twenty percent. How many grapes does he need in a year after increasing his production?"""
    grapes_per_six_months = 90
    increase_percent = 20
    grapes_per_year = grapes_per_six_months * 2 * (1 + (increase_percent / 100))
    result = grapes_per_year
    return result

print(solution())