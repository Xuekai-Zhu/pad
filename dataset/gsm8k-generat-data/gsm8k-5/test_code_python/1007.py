def solution():
    total_distance = 25  # Together, they walked 25 kilometers
    hiro_distance = x  # Let's assume Hiro walked x kilometers

    # Rajesh walked 10 kilometers less than 4 times Hiro's distance
    rajesh_distance = (4 * hiro_distance) - 10

    # The total distance walked is the sum of Hiro and Rajesh's distance
    total_distance_walked = hiro_distance + rajesh_distance

    # Solve for x
    x = (total_distance - 10) / 5

    # Solve for Rajesh's distance
    rajesh_distance = (4 * x) - 10
    result = rajesh_distance
    return result

print(solution())