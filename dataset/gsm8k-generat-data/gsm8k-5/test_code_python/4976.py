def solution():
    # Calculate the total amount of water already in the glasses
    total_water = 6 * 10 * (4/5)  # 6 ounces per glass, 10 glasses, and 4/5 full

    # Calculate the amount of water needed to fill the glasses to the brim
    total_capacity = 6 * 10  # The glasses have a capacity of 6 ounces each, and there are 10 glasses
    needed_water = total_capacity - total_water

    result = needed_water
    return result

print(solution())