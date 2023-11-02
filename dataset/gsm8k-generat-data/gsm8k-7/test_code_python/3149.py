def solution():
    total_length = 30

    # Calculate the length of each equal part
    part_length = total_length / 6

    # Calculate the length of the ribbon used
    used_length = part_length * 4

    # Calculate the length of the ribbon not used
    not_used_length = total_length - used_length
    result = not_used_length
    return result

print(solution())