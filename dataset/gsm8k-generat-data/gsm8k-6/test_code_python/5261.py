def solution():
    # Calculate the amount of water needed to fill the pool
    pool_volume = 10 * 10 * 6  # the pool measures 10 ft x 10 ft x 6 ft
    water_for_pool = pool_volume  # each gallon of water fills 1 cubic foot of the pool

    # Calculate the amount of water Jerry can use for showers
    water_for_showering = 1000 - 100 - water_for_pool  # Jerry has 1000 gallons in total and uses 100 for drinking and cooking

    # Calculate how many showers Jerry can take
    showers = water_for_showering / 20  # Jerry uses 20 gallons per shower
    result = int(showers)  # convert to integer for whole number of showers
    return result

print(solution())