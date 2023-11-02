def solution():
    # Calculate the length of the straight part of the river
    crooked_length = 80  # given the total length of the river is 80 miles
    straight_length = crooked_length / 4  # given the straight part is three times shorter than the crooked part
    result = straight_length
    return result

print(solution())