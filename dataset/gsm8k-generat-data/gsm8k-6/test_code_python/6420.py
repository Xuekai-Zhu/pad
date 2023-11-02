def solution():
    # Calculate the total distance Rich walked
    total_distance = 20 + 200 + 2*(20 + 200) + (20 + 200 + 2*(20 + 200))/2
    # Rich walks double his total distance so far after turning left and walks half the distance back to reach his starting point
    total_distance *= 2.5
    result = total_distance
    return result

print(solution())