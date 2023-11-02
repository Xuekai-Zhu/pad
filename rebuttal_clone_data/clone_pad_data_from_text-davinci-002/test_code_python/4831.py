def solution():
    previous_property_size = 2
    new_property_size = 10 * previous_property_size
    pond_size = 1
    usable_property_size = new_property_size - pond_size
    result = usable_property_size
    return result

print(solution())