def solution():
    current_length = 14
    wig_length = 23
    desired_length = 12

    total_length_needed = current_length - desired_length + wig_length
    length_left_to_grow = total_length_needed - current_length
    result = length_left_to_grow
    return result

print(solution())