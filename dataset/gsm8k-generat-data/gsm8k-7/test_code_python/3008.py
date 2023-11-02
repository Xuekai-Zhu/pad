def solution():
    snake_length = 10  # feet
    head_length = snake_length / 10
    body_length = snake_length - head_length

    # Calculate the length of the rest of the body minus the head
    rest_of_body_length = body_length - head_length
    result = rest_of_body_length
    return result

print(solution())