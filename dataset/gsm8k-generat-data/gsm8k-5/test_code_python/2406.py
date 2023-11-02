def solution():
    total_rooms = 72  # The entire space station has 72 rooms
    rooms_per_cylinder = 12 + 7 + x  # Each cylindrical structure contains 12 bedrooms, 7 bathrooms, and x kitchens
    cylinders = 3  # There are 3 identical cylindrical structures

    # Calculate the total number of kitchens on the entire space station
    total_kitchens = cylinders * rooms_per_cylinder - total_rooms  # We subtract the total rooms to get only the kitchens
    result = total_kitchens
    return result

print(solution())