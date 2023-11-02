def solution():
     """Borris liquor store uses 90 kilograms of grapes every 6 months. He is thinking of increasing his production by twenty percent. How many grapes does he need in a year after increasing his production?"""
    grapes_per_six_months = 90
    increased_percentage = 20
    increased_grapes_amount =  (grapes_per_six_months / 100) * increased_percentage
    grapes_per_year = grapes_per_six_months + increased_grapes_amount
    result = grapes_per_year
    return result

print(solution())