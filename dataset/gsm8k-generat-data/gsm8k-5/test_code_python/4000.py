def solution():
    jenny_distance = 18 + (1/3)*18  # Jenny's bottlecap travels 18 feet straight and then 1/3 of that distance again
    mark_distance = 15 + 2*15  # Mark's bottlecap travels 15 feet and then twice that distance again
    difference = mark_distance - jenny_distance  # Calculate the difference between the two distances
    result = difference
    return result

print(solution())