def solution():
    # Define the length of the snake and the ratio of the head to the body
    snake_length = 10
    head_ratio = 1/10

    # Calculate the length of the head
    head_length = snake_length * head_ratio

    # Calculate the length of the rest of the body
    body_length = snake_length - head_length

    # Subtract the head length from the body length to get the result
    result = body_length - head_length
    return result

print(solution())