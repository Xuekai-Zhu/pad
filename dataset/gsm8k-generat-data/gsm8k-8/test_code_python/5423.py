def solution():
    # Calculate the total distance to the park and back
    total_distance = (10 + 4) * 2

    # Subtract the walking distance from the total distance to find the skateboarding distance
    skateboarding_distance = total_distance - 4

    result = skateboarding_distance
    return result

print(solution())