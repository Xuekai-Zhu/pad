def solution():
    """Mia can decorate 2 dozen Easter eggs per hour. Her little brother Billy can only decorate 10 eggs per hour. They need to decorate 170 eggs for the Easter egg hunt. If they work together, how long will it take them to decorate all the eggs?"""
    # Define the number of eggs to be decorated
    eggs_to_decorate = 170

    # Define the rate of decoration for Mia and Billy
    mia_rate = 2 * 12  # Mia can decorate 2 dozen eggs per hour, or 24 eggs per hour
    billy_rate = 10

    # Calculate the combined rate of decoration
    combined_rate = mia_rate + billy_rate

    # Calculate the time needed to decorate all the eggs
    time_needed = eggs_to_decorate / combined_rate

    # Return the result rounded to the nearest integer
    result = round(time_needed)
    return result

print(solution())