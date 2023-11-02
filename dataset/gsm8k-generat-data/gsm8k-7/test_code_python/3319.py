def solution():
    total_yarn_length = 10
    num_parts = 5
    parts_used = 3

    # Calculate the length of one part
    part_length = total_yarn_length / num_parts

    # Calculate the total length used for crocheting
    crocheting_length = parts_used * part_length
    result = crocheting_length
    return result

print(solution())