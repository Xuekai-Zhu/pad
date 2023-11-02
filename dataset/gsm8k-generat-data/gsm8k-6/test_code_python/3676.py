def solution():
    # Calculate the amount of honey used per night
    honey_per_night = 1 * 2  # Tabitha adds 1 serving of honey per cup of tea, and she usually has 2 cups of tea before bed
    
    # Calculate the amount of honey used per ounce
    honey_per_ounce = 6
    
    # Calculate the amount of honey used in total
    total_honey_used = honey_per_night / honey_per_ounce
    
    # Calculate the number of nights Tabitha can enjoy honey in her tea before running out
    nights_with_honey = 16 / total_honey_used
    result = nights_with_honey
    return result

print(solution())