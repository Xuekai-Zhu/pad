def solution():
    # Calculate the total area of fabric needed for curtains
    living_room_area = 4 * 6 # square feet
    bedroom_area = 2 * 4 # square feet
    total_area = living_room_area + bedroom_area # square feet

    # Calculate the area of the remaining fabric
    remaining_area = (16 * 12) - total_area # square feet
    result = remaining_area
    return result

print(solution())