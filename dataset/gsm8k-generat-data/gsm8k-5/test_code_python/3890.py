def solution():
    distance_per_buoy = 24  # Assuming evenly spaced buoys, each buoy is 24 meters away from the previous one
    distance_to_third_buoy = 72  # The swimmer has already swum 72 meters to get to the third buoy

    # Calculate the distance to the fourth buoy
    distance_to_fourth_buoy = distance_to_third_buoy + distance_per_buoy

    result = distance_to_fourth_buoy
    return result

print(solution())