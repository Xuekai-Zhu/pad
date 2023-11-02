def solution():
    total_length = 100  # Marty has 100 centimeters of ribbon
    num_parts = 4  # Marty needs to cut into 4 equal parts
    num_parts_per_part = 5  # Each part must be divided into 5 equal parts

    # Calculate the length of each part
    part_length = total_length / num_parts_per_part

    # Calculate the length of each final cut
    final_cut_length = part_length / num_parts_per_part
    result = final_cut_length
    return result

print(solution())