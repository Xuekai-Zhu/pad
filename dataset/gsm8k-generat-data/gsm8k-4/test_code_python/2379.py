def solution():
    """Carla needs to bring water to her animals. Each horse needs twice as much water as a pig, and the chickens drink from one tank that needs 30 gallons. How many gallons of water does Carla need to bring if she has 8 pigs and 10 horses and each pig needs 3 gallons of water?"""
    # Define the number of pigs and horses
    num_pigs = 8
    num_horses = 10

    # Calculate the total amount of water needed for the pigs
    pig_water = num_pigs * 3

    # Calculate the total amount of water needed for the horses
    horse_water = num_horses * 6

    # Calculate the total amount of water needed
    total_water = pig_water + horse_water + 30

    # return the result
    result = total_water
    return result

print(solution())