def solution():
    """4.5 gallons of coffee were divided among 18 thermoses. Genevieve drank 3 thermoses. How many pints of coffee did Genevieve drink?"""
    # Define the total amount of coffee and the number of thermoses
    total_coffee = 4.5 * 128  # Convert gallons to pints
    num_thermoses = 18

    # Calculate the amount of coffee in each thermos
    coffee_per_thermos = total_coffee / num_thermoses

    # Calculate the amount of coffee Genevieve drank
    genevieve_coffee = coffee_per_thermos * 3

    # Convert the amount of coffee Genevieve drank from pints to gallons
    genevieve_coffee = genevieve_coffee / 128

    # Round the result to 1 decimal place
    result = round(genevieve_coffee, 1)
    return result

print(solution())