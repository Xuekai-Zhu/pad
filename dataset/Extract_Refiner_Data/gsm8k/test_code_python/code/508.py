def solution():
    
    # Define the amount of water Hannah needs to drink per kilometer
    WATER_PER_KG = 60

    # Define the number of laps Hannah needs to run
    NUM_LEAPS = 8

    # Define the distance Hannah needs to run
    distance = 0.25 * NUM_LEAPS

    # Calculate the total amount of water Hannah needs to drink
    total_water = distance * WATER_PER_KG

    # Display the total amount of water Hannah needs to drink
    result = total_water
    return result

print(solution())