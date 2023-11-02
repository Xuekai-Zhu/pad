def solution():
    """Miss Aisha's legs are 1/3 of her total height. If her head is also 1/4 of her total height, and she is 60 inches tall, calculate the length of the rest of her body."""
    height = 60
    leg_length = height * 1/3
    head_length = height * 1/4
    body_length = height - leg_length - head_length
    result = body_length
    return result

print(solution())