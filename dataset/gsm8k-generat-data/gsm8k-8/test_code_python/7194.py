def solution():
    # Define Julien's distance
    julien_distance = 50

    # Calculate Sarah's distance
    sarah_distance = julien_distance * 2

    # Calculate Jamir's distance
    jamir_distance = sarah_distance + 20

    # Calculate the total distance for the week
    total_distance = (julien_distance + sarah_distance + jamir_distance) * 7

    result = total_distance
    return result

print(solution())