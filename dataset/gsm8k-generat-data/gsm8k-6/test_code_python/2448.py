def solution():
    # Calculate the total amount of water in all the bottles
    water_per_bottle = (3/4) * 12  # each bottle is filled up to 3/4 of its capacity
    total_bottles = 10 * 50  # 10 boxes with 50 bottles each
    total_water = water_per_bottle * total_bottles  # total water in all the bottles
    result = total_water
    return result

print(solution())