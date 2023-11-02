def solution():
    third_segment_length = 10

    # Calculate the length of the second segment
    second_segment_length = third_segment_length * 2

    # Calculate the length of the first segment
    first_segment_length = second_segment_length * 2

    # Calculate the total length of the show
    total_length = first_segment_length + second_segment_length + third_segment_length
    result = total_length
    return result

print(solution())