def solution():
    total_guests = 90  # There were 90 people at the picnic
    sodas = 50  # There were 50 soda cans
    sparkling_waters = 50  # There were 50 plastic bottles of sparkling water
    juices = 50  # There were 50 glass bottles of juice

    # Calculate how many guests drank soda
    soda_drinkers = total_guests / 2

    # Calculate how many guests drank sparkling water
    sparkling_water_drinkers = total_guests / 3

    # Calculate how many juices were consumed
    consumed_juices = 4 * juices / 5

    # Calculate the total number of recyclable cans and bottles
    total_recyclables = (soda_drinkers * 1) + (sparkling_water_drinkers * 1) + (consumed_juices * 1)

    result = total_recyclables
    return result

print(solution())