def solution():
    # Calculate the distance Carson walks in one circle around the warehouse
    circle_distance = 2 * (600 + 400)  # distance around a rectangle = 2*(length + width)

    # Calculate the total distance Carson is supposed to walk in one night
    total_distance = 10 * circle_distance

    # Calculate the distance Carson actually walks, after skipping 2 circles
    actual_distance = total_distance - 2 * circle_distance
    result = actual_distance
    return result

print(solution())