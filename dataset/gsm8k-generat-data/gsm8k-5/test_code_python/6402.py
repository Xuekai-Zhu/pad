def solution():
    lime_juice_per_mocktail = 1/16  # Julio uses 1 tablespoon of lime juice per mocktail
    sparkling_water_per_mocktail = 1  # Julio uses 1 cup of sparkling water per mocktail
    limes_per_mocktail = 1/2  # Julio needs half a lime for each mocktail
    mocktails_per_day = 1  # Julio makes 1 mocktail per day
    days = 30  # Julio wants to know how much he will spend on limes in 30 days
    price_per_lime = 1/3  # Limes cost 3 for $1.00

    # Calculate the total number of limes Julio will need in 30 days
    total_limes = lime_juice_per_mocktail * mocktails_per_day * days * 2  # Julio can get 2 tablespoons of lime juice per lime

    # Calculate the total cost of the limes
    total_cost = total_limes * limes_per_mocktail * price_per_lime
    result = total_cost
    return result

print(solution())