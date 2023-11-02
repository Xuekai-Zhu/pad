def solution():
    seawater_volume = 2  # Jack collects 2 liters of seawater
    salt_concentration = 0.20  # The seawater is 20% salt

    # Calculate the volume of salt in the seawater
    salt_volume = seawater_volume * salt_concentration

    # Convert the salt volume to milliliters
    salt_ml = salt_volume * 1000
    result = salt_ml
    return result

print(solution())