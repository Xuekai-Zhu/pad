def solution():
    """Carla needs to bring water to her animals. Each horse needs twice as much water as a pig, and the chickens drink from one tank that needs 30 gallons. How many gallons of water does Carla need to bring if she has 8 pigs and 10 horses and each pig needs 3 gallons of water?"""
    # Define the amount of water needed for each animal
    PIG_WATER = 3
    HORSE_WATER = 2 * PIG_WATER

    # Define the number of each animal
    num_pigs = 8
    num_horses = 10

    # Calculate the total amount of water needed for the pigs
    pig_water_total = num_pigs * PIG_WATER

    # Calculate the total amount of water needed for the horses
    horse_water_total = num_horses * HORSE_WATER

    # Calculate the total amount of water needed
    total_water = pig_water_total + horse_water_total + 30

    # Display the total amount of water needed
    result = total_water
    return result

print(solution())