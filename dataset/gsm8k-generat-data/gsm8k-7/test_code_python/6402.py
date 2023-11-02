def solution():
    tablespoons_per_mocktail = 1
    cups_per_mocktail = 1
    tablespoons_per_lime = 2
    num_days = 30
    limes_price = 1/3  # cost of one lime

    # Calculate the total number of mocktails Julio will make
    total_mocktails = num_days

    # Calculate the total number of tablespoons of lime juice needed
    total_lime_juice = total_mocktails * tablespoons_per_mocktail

    # Calculate the total number of limes needed
    total_limes = total_lime_juice / tablespoons_per_lime

    # Calculate the total cost of all limes needed
    total_cost = total_limes * limes_price
    result = total_cost
    return result

print(solution())