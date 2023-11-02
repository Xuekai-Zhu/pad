def solution():
    # Calculate the length of the second interview segment
    length_3rd_segment = 10
    length_2nd_segment = length_3rd_segment * 2  # the third interview segment is always half as long as the second

    # Calculate the length of the first interview segment
    length_1st_segment = length_2nd_segment * 2  # the first interview segment is always twice as long as the other two segments combined

    # Calculate the total length of the show
    total_length = length_1st_segment + length_2nd_segment + length_3rd_segment
    result = total_length
    return result

print(solution())