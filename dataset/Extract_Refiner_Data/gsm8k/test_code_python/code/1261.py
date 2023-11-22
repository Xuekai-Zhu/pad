def solution():
    
    # Define the amount of juice needed for one gallon of lemonade
    LEMONADE_PER_GALLON = 1

    # Define the number of gallons of lemonade needed
    gallons_needed = 4

    # Calculate the amount of juice needed for the extra gallon of lemonade
    extra_gallon_juice = 2 * LEMONADE_PER_GALLON

    # Calculate the total amount of juice needed
    total_juice_needed = gallons_needed - extra_gallon_juice

    # Calculate the number of lemons needed
    lemons_needed = total_juice_needed // LEMONADE_PER_GALLON

    # Display the number of lemons needed
    result = lemons_needed
    return result

print(solution())