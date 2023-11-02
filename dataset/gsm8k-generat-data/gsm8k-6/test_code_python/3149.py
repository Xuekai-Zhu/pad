def solution():
    # Calculate the length of each part of the ribbon
    part_length = 30 / 6

    # Calculate the total length of ribbon used
    used_length = 4 * part_length

    # Calculate the length of ribbon not used
    not_used_length = 30 - used_length
    result = not_used_length
    return result

print(solution())