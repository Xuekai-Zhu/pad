def solution():
    # Calculate the length of one part of the wire
    length_one_part = 50 / 5

    # Calculate the length of the wire used
    length_used = length_one_part * 3

    # Calculate the length of the wire not used
    length_not_used = 50 - length_used
    result = length_not_used
    return result

print(solution())