def solution():
    average_cows_per_production = 6
    liters_of_milk_per_production = 108
    total_liters_of_milk = 2160
    total_weeks = 5
    
    # Calculate the total number of productions
    total_productions = total_liters_of_milk / (average_cows_per_production * liters_of_milk_per_production)

    # Calculate the total number of cows
    total_cows = total_productions / total_weeks
    result = total_cows
    return result

print(solution())