def solution():
    """Debra is the host of a country music radio show, and she broadcasts interviews with celebrity country music singers. Each week, she interviews three singers, one at a time.  The first interview segment is always twice as long as the other two segments combined, and the third interview segment is always half as long as the second. If the third segment is 10 minutes long, how many minutes long is the entire show?"""
    # Calculate the length of the third segment
    third_segment = 10

    # Calculate the length of the second segment
    second_segment = third_segment * 2

    # Calculate the length of the first segment
    first_segment = (second_segment + third_segment) * 2

    # Calculate the total length of the show
    total_length = first_segment + second_segment + third_segment

    # Return the result
    result = total_length
    return result

print(solution())