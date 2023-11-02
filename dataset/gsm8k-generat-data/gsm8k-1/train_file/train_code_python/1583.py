def solution():
    """Debra is the host of a country music radio show, and she broadcasts interviews with celebrity country music singers. Each week, she interviews three singers, one at a time. The first interview segment is always twice as long as the other two segments combined, and the third interview segment is always half as long as the second. If the third segment is 10 minutes long, how many minutes long is the entire show?"""
    third_segment = 10
    second_segment = third_segment * 2
    first_segment = (second_segment + third_segment) * 2
    total_length = first_segment + second_segment + third_segment
    result = total_length
    return result

print(solution())