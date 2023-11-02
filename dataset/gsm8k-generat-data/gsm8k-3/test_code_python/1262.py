def solution():
    """4.5 gallons of coffee were divided among 18 thermoses. Genevieve drank 3 thermoses. How many pints of coffee did Genevieve drink?"""
    # Define the total amount of coffee in gallons and the number of thermoses
    TOTAL_COFFEE_GAL = 4.5
    NUM_THERMOSES = 18

    # Calculate the amount of coffee per thermos in gallons
    coffee_per_thermos_gal = TOTAL_COFFEE_GAL / NUM_THERMOSES

    # Calculate the amount of coffee Genevieve drank in gallons
    genevieve_coffee_gal = coffee_per_thermos_gal * 3

    # Convert gallons to pints
    genevieve_coffee_pints = genevieve_coffee_gal * 8

    # Display the amount of coffee Genevieve drank in pints
    result = genevieve_coffee_pints
    return result

print(solution())