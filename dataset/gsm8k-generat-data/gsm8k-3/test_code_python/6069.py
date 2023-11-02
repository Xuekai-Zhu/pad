def solution():
    """Mia can decorate 2 dozen Easter eggs per hour. Her little brother Billy can only decorate 10 eggs per hour. They need to decorate 170 eggs for the Easter egg hunt. If they work together, how long will it take them to decorate all the eggs?"""
    # Define the rate of egg decoration for Mia and Billy
    MIA_RATE = 24 * 2
    BILLY_RATE = 10

    # Calculate the combined rate of egg decoration
    combined_rate = MIA_RATE + BILLY_RATE

    # Calculate the time it will take to decorate all the eggs
    time = 170 / combined_rate

    # Display the time
    result = time
    return result

print(solution())