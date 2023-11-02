def solution():
    # Define the total race distance and the distance of the first three parts
    total_distance = 74.5
    first_part = 15.5
    second_and_third_parts = 2 * 21.5

    # Subtract the distance of the first three parts to find the distance of the last part
    last_part = total_distance - first_part - second_and_third_parts
    result = last_part
    return result

print(solution())