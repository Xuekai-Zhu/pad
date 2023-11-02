def solution():
    # Calculate the distance traveled by Johny to the East
    east_distance = 40 + 20  # 20 more miles than the distance he took to travel to the South

    # Calculate the total distance traveled by Johny
    total_distance = 40 + east_distance + (2 * east_distance)  # he turned North and traveled twice the distance he had traveled to the East
    result = total_distance
    return result

print(solution())