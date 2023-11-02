def solution():
    total_distance = 1000  # Matt rode a total of 1000 feet
    distance_to_first_sign = 350  # The first stop sign was 350 feet away from his house
    distance_to_second_sign = total_distance - (distance_to_first_sign + 275)  # Calculate the distance between the two signs

    result = distance_to_second_sign - distance_to_first_sign  # Calculate the distance between the first and second signs
    return result

print(solution())