def solution():
    # Calculate the length of hair after cutting off half
    half_length = 24 / 2

    # Calculate the length of hair after growing 4 more inches
    grow_length = half_length + 4

    # Calculate the final length of hair after cutting off 2 more inches
    final_length = grow_length - 2

    result = final_length
    return result

print(solution())