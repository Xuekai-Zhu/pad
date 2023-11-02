def solution():
    fraction_full = 1/3  # The tank shows that it is 1/3 full
    additional_water = 16  # 16 gallons of water are added to fill the tank

    # Calculate how much water was already in the tank
    original_water = additional_water / (1 - fraction_full)
    # subtracting 1 from the fraction_full because the fraction given is the fraction empty
    # and we need to get the fraction full

    # Calculate the total capacity of the tank
    tank_capacity = original_water + additional_water
    result = tank_capacity
    return result

print(solution())