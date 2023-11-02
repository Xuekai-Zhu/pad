def solution():
    third_segment = 10  # Third segment is 10 minutes long
    second_segment = third_segment * 2  # Second segment is twice as long as the third
    first_segment = (second_segment + third_segment) * 2  # First segment is twice as long as the other two combined

    # Calculate the total length of the show
    total_length = first_segment + second_segment + third_segment
    result = total_length
    return result

print(solution())