def solution():
    
    # Define the number of plants and the amount of water needed for each type of plant
    NUM_PLANTS = 20
    HALF_WATER_PER_PLANT = 0.5
    ONE_WATER_PER_PLANT = 1
    QUARTER_WATER_PER_PLANT = 0.25

    # Calculate the total amount of water needed for the plants
    total_water_needed = (4 * HALF_WATER_PER_PLANT) + (8 * ONE_WATER_PER_PLANT) + (NUM_PLANTS - 4 - 8) * QUARTER_WATER_PER_PLANT

    # Display the total amount of water needed
    result = total_water_needed
    return result

print(solution())