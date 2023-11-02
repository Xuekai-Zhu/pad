def solution():
    """Julio makes a mocktail every evening. He uses 1 tablespoon of lime juice and tops with 1 cup of sparkling water. He can usually squeeze 2 tablespoons of lime juice per lime. After 30 days, if limes are 3 for $1.00, how much will he have spent on limes?"""
    # Define the amount of lime juice and sparkling water used per day
    lime_juice_per_day = 1
    sparkling_water_per_day = 1

    # Define the amount of lime juice squeezed from each lime
    lime_juice_per_lime = 2

    # Calculate the total amount of lime juice used in 30 days
    total_lime_juice = lime_juice_per_day * 30

    # Calculate the number of limes needed to make the total amount of lime juice
    total_limes = total_lime_juice / lime_juice_per_lime

    # Calculate the total cost of the limes
    cost_per_lime = 1/3
    total_cost = cost_per_lime * total_limes

    # Round the total cost to two decimal places
    result = round(total_cost, 2)
    return result

print(solution())