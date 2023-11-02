def solution():
    """Miss Aisha's legs are 1/3 of her total height. If her head is also 1/4 of her total height, and she is 60 inches tall, calculate the length of the rest of her body."""
    # Calculate the total length of Miss Aisha's legs
    leg_length = 60 * (1/3)

    # Calculate the total length of Miss Aisha's head
    head_length = 60 * (1/4)

    # Calculate the total length of Miss Aisha's body
    body_length = 60 - leg_length - head_length

    # Return the result
    result = body_length
    return result

print(solution())