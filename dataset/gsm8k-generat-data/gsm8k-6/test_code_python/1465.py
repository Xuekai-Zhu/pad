def solution():
    # Calculate the total distance Jack moved in inches
    up_distance = 3 * 12 * 8  # Jack went up three flights of stairs, each with 12 steps of 8 inches
    down_distance = 6 * 12 * 8  # Jack went down six flights of stairs, each with 12 steps of 8 inches
    total_distance = down_distance - up_distance  # Jack went further down than where he started
    # Convert the total distance to feet
    distance_in_feet = total_distance / 12
    result = distance_in_feet
    return result

print(solution())