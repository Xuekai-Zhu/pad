def solution():
    previous_property = 2  # acres
    new_property = previous_property * 10  # 10 times larger
    pond = 1  # acre pond

    # Calculate the size of the land that is suitable for growing vegetables
    vegetable_land = new_property - pond
    result = vegetable_land
    return result

print(solution())