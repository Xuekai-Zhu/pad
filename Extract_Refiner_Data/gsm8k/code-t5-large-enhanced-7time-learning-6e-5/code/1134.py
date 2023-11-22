def solution():
    
    # Define the initial number of cows and chickens
    initial_cows = 50
    initial_chickens = 20

    # Define the number of days in three weeks
    days_in_weeks = 7

    # Calculate the number of cows and chickens brought in in three weeks
    cows_per_week = 20 * days_in_weeks
    chickens_per_week = 10 * days_in_weeks

    # Calculate the total number of cows and chickens on the farm after three weeks
    total_cows = initial_cows + cows_per_week
    total_chickens = initial_chickens + chickens_per_week

    # Calculate the total number of animals on the farm after three weeks
    total_animals = total_cows + total_chickens

    # return the result
    result = total_animals
    return result

print(solution())