def solution():
    # Calculate the distance Sadie runs
    sadie_distance = 3 * 2  # Average speed of 3 miles per hour for 2 hours

    # Calculate the distance Ariana runs
    ariana_distance = 6 * 0.5  # Speed of 6 miles per hour for 0.5 hours

    # Calculate the time and distance for Sarah's section
    sarah_time = 4.5 - 2.5  # Total race time minus time spent by Sadie and Ariana
    sarah_distance = sarah_time * 4  # Average speed of 4 miles per hour for time spent by Sarah

    # Calculate the total distance of the race
    total_distance = sadie_distance + ariana_distance + sarah_distance
    result = total_distance
    return result

print(solution())