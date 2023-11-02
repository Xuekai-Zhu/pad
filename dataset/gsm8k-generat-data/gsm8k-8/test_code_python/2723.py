def solution():
    # Define the total length of the river
    total_length = 80

    # Calculate the length of the crooked part of the river
    crooked_length = total_length / 4

    # Calculate the length of the straight part of the river
    straight_length = 3 * crooked_length

    result = straight_length
    return result

print(solution())