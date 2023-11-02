def solution():
    # Define the number of beakers and the number of beakers with copper ions in them
    total_beakers = 22
    copper_beakers = 8

    # Define the number of drops it takes to turn a beaker with copper ions blue
    copper_drops = 3

    # Calculate the total drops needed to find all beakers with copper ions
    total_copper_drops = copper_beakers * copper_drops

    # Calculate the number of beakers without copper ions tested
    beakers_without_copper = (total_copper_drops - 45) / 3

    result = beakers_without_copper
    return result

print(solution())