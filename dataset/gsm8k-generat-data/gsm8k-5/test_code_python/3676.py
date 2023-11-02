def solution():
    servings_per_cup = 1  # Tabitha adds 1 serving of honey per cup of tea
    cups_per_night = 2  # Tabitha has 2 cups of tea before bed
    ounces_per_container = 16  # The honey container holds 16 ounces
    servings_per_ounce = 6  # There are 6 servings of honey per ounce

    # Calculate the total servings of honey Tabitha will use per night
    total_servings_per_night = servings_per_cup * cups_per_night

    # Calculate how many servings of honey Tabitha will use in total
    total_servings = total_servings_per_night * 365  # Tabitha has tea every night for a year

    # Calculate how many ounces of honey Tabitha will need in total
    total_ounces = total_servings / servings_per_ounce

    # Calculate how many nights Tabitha will be able to enjoy honey in her tea before bed
    nights_of_honey = total_ounces / ounces_per_container
    result = nights_of_honey
    return result

print(solution())