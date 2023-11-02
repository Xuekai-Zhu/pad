def solution():
    # Define the amount of seawater collected and its salt concentration
    seawater_volume = 2000 # in ml
    salt_concentration = 0.2 # 20% in decimal form

    # Calculate the amount of salt in the seawater
    salt_volume = seawater_volume * salt_concentration

    result = salt_volume
    return result

print(solution())