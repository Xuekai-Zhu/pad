def solution():
    """Debra is the host of a country music radio show, and she broadcasts interviews with celebrity country music singers. Each week, she interviews three singers, one at a time.  The first interview segment is always twice as long as the other two segments combined, and the third interview segment is always half as long as the second. If the third segment is 10 minutes long, how many minutes long is the entire show?"""
    # Define the length of the third interview segment
    segment_3 = 10

    # Calculate the length of the second interview segment
    segment_2 = segment_3 * 2

    # Calculate the length of the first interview segment
    segment_1 = 2 * (segment_2 + segment_3)

    # Calculate the total length of the show
    total_length = segment_1 + segment_2 + segment_3

    # Display the total length of the show
    result = total_length
    return result

print(solution())