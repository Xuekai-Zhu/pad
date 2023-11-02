def solution():
    previous_property = 2  # Joyce's previous property size was 2 acres
    new_property = 10 * previous_property  # Joyce's new property is 10 times larger than her previous property
    pond_size = 1  # Joyce's new property has a 1-acre pond where she cannot grow vegetables

    # Calculate the size of the land suitable for growing vegetables
    vegetable_land = new_property - pond_size
    result = vegetable_land
    return result

print(solution())