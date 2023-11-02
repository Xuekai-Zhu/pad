def solution():
    # Calculate the length of the head of the snake
    head_length = 10 * 0.1  # one-tenth of its length

    # Calculate the length of the rest of its body
    body_length = 10 - head_length

    result = body_length
    return result

print(solution())