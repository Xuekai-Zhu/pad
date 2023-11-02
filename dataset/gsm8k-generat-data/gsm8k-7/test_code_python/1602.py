def solution():
    total_distance = 8205
    monday_distance = 907
    tuesday_distance = 582

    # Calculate the total distance Amelia has driven so far
    driven_distance = monday_distance + tuesday_distance

    # Calculate the distance remaining to cross the country
    remaining_distance = total_distance - driven_distance
    result = remaining_distance
    return result

print(solution())