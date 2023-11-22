def solution():
    
    # Define the original temperature and the percentage off
    ORIGINAL_TEMP = 450
    DISCOUNT_PERCENTAGE = 0.2

    # Calculate the temperature using the recipe's temperature
    temperature = ORIGINAL_TEMP / 520

    # Calculate the percentage off
    percentage_off = temperature * DISCOUNT_PERCENTAGE

    # Calculate the temperature needed to reach the actual temperature
    temperature_needed = temperature - percentage_off

    # Display the temperature needed
    result = temperature_needed
    return result

print(solution())