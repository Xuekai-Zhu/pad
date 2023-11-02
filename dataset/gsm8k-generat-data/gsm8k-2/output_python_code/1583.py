def solution():
    """Debra is the host of a country music radio show, and she broadcasts interviews with celebrity country music singers. Each week, she interviews three singers, one at a time. The first interview segment is always twice as long as the other two segments combined, and the third interview segment is always half as long as the second. If the third segment is 10 minutes long, how many minutes long is the entire show?"""
    third_segment_length = 10
    second_segment_length = 2 * third_segment_length
    first_segment_length = 2 * second_segment_length - second_segment_length - third_segment_length
    total_show_length = first_segment_length + second_segment_length + third_segment_length
    result = total_show_length
    return result

print(solution())