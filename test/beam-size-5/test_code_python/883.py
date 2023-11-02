def solution():
    
    # Define the number of birds in the bushes
    birds_in_bushes = 6

    # Calculate the number of birds flying overhead
    flying_overhead_birds = birds_in_bushes * (2/3)

    # Calculate the number of birds in the feeding
    feeding_birds = 3 * 8

    # Calculate the total number of birds counted
    total_birds = birds_in_bushes + flying_overhead_birds + feeding_birds

    # Display the total number of birds counted
    result = total_birds
    return result

print(solution())