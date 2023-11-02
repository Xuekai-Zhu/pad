def solution():
    # Define the initial number of horses and their daily water consumption
    num_horses = 3
    water_per_day = (5+2) * num_horses

    # Calculate the total water consumption for all horses for 28 days
    total_water = water_per_day * num_horses * 28

    # Add the water consumption for the additional horses
    num_additional_horses = 5
    additional_water_per_day = (5+2) * num_additional_horses
    total_water += additional_water_per_day * num_additional_horses * 28

    result = total_water
    return result

print(solution())