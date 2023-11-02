def solution():
    # Define the length of the third segment
    segment3_length = 10

    # Calculate the length of the second segment
    segment2_length = segment3_length * 2

    # Calculate the length of the first segment
    segment1_length = segment2_length * 2

    # Calculate the total length of the show
    total_length = segment1_length + segment2_length + segment3_length
    result = total_length
    return result

print(solution())