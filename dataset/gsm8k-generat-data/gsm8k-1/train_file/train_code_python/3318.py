def solution():
    """A 10 meters yarn was cut into 5 equal parts. If 3 parts were used for crocheting, how long was used for crocheting?"""
    total_length = 10
    num_parts = 5
    length_per_part = total_length / num_parts
    parts_used = 3
    length_used = parts_used * length_per_part
    result = length_used
    return result

print(solution())