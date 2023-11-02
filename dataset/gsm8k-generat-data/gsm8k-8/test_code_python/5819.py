def solution():
    # Calculate the total amount of water needed for the corn plants
    corn_water = (4 * 15 * 0.5)  # 30 gallons

    # Calculate the total amount of water needed for the pigs
    pig_water = 10 * 4  # 40 gallons

    # Calculate the total amount of water needed for the ducks
    duck_water = 20 * 0.25  # 5 gallons

    # Calculate the total amount of water needed
    total_water = corn_water + pig_water + duck_water

    # Calculate the time needed to pump the water
    time_needed = total_water / 3  # in minutes

    result = time_needed
    return result

print(solution())