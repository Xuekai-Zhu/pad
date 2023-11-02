def solution():
    volume_seawater = 2 * 1000  # convert 2 liters to milliliters
    salt_concentration = 0.20  # 20% salt

    # Calculate the total amount of salt in the seawater
    total_salt = volume_seawater * salt_concentration

    result = total_salt
    return result

print(solution())