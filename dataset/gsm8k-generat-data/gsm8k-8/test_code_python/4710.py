def solution():
    # Define the distance between Arizona and New York
    plane_distance = 2000

    # Calculate the distance between Arizona and Missouri by driving
    driving_distance_AZ_MO = plane_distance * 1.4 / 2

    # Calculate the total distance between Arizona and New York by driving
    driving_distance = driving_distance_AZ_MO * 2

    # Calculate the distance between Missouri and New York by driving
    driving_distance_MO_NY = driving_distance - driving_distance_AZ_MO

    result = driving_distance_MO_NY
    return result

print(solution())