def solution():
    cd1_length = 1.5  # Length of first CD in hours
    cd2_length = 1.5  # Length of second CD in hours
    cd3_length = 2 * cd1_length  # Length of third CD in hours (twice the length of first CD)

    # Calculate the total length of all three CDs
    total_length = cd1_length + cd2_length + cd3_length
    result = total_length
    return result

print(solution())