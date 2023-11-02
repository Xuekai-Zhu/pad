def solution():
    """Carson is refilling his tires. Each tire can hold 500 cubic inches of air. Two of the tires are completely flat and empty. One tire is 40% full and the last tire is 70% full. If Carson injects 50 cubic inches of air with each pump, how many pumps will it take him to fill all the tires?"""
    # Define the volume each tire can hold
    TIRE_VOLUME = 500

    # Calculate the volume of air needed to fill the two completely flat tires
    flat_tires_volume = 2 * TIRE_VOLUME

    # Calculate the volume of air needed to fill the 40% full tire
    tire_40_volume = 0.4 * TIRE_VOLUME

    # Calculate the volume of air needed to fill the 70% full tire
    tire_70_volume = 0.7 * TIRE_VOLUME

    # Calculate the total volume of air needed
    total_volume = flat_tires_volume + (TIRE_VOLUME - tire_40_volume) + (TIRE_VOLUME - tire_70_volume)

    # Calculate the number of pumps needed
    num_pumps = total_volume / 50

    # Round up to the nearest whole number of pumps
    num_pumps = math.ceil(num_pumps)

    # Display the number of pumps needed
    result = num_pumps
    return result

print(solution())