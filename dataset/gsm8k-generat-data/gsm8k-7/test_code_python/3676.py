def solution():
    servings_per_ounce = 6
    ounces_per_container = 16
    servings_per_cup = 1
    cups_per_night = 2
    
    # Calculate the total servings of honey used per night
    total_servings_per_night = servings_per_cup * cups_per_night
    
    # Calculate the total servings of honey used for all nights
    total_servings = 0
    while ounces_per_container > 0:
        servings_in_ounce = ounces_per_container * servings_per_ounce
        if servings_in_ounce < total_servings_per_night:
            total_servings += servings_in_ounce
            total_servings_per_night -= servings_in_ounce
            ounces_per_container = 0
        else:
            total_servings += total_servings_per_night
            ounces_per_container -= 1
    
    # Calculate the number of nights she can enjoy honey in her tea before the container runs out
    num_nights = total_servings // (servings_per_cup * cups_per_night)
    result = num_nights
    return result

print(solution())