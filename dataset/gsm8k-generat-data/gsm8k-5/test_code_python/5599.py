def solution():
    # Calculate the distance Mairead walks
    distance_walked = (3/5) * 40  # Mairead walks 3/5 times the distance she ran

    # Calculate the distance Mairead jogs
    distance_jogged = distance_walked / 5  # Mairead walks 5 times the distance she jogged

    # Calculate the total distance Mairead covered
    total_distance = 40 + distance_walked + distance_jogged
    result = total_distance
    return result

print(solution())