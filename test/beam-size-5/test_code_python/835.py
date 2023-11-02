def solution():
    
    # Define the daily milk production and the number of cows
    daily_milk_production = 5
    num_cows = 3

    # Define the target milk production
    target_milk_production = 25

    # Calculate the total milk production needed per day
    total_milk_production_needed = target_milk_production - (daily_milk_production * num_cows)

    # Calculate the number of additional cows needed to reach the target milk production
    additional_cows_needed = total_milk_production_needed / daily_milk_production

    # Return the result
    result = additional_cows_needed
    return result

print(solution())