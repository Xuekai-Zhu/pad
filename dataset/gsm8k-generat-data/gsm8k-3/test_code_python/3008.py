def solution():
    """A snake's head is one-tenth its length. If a snake is 10 feet long, calculate the length of the rest of its body minus the head."""
    # Define the length of the snake and the ratio of the head to the total length
    snake_length = 10
    head_ratio = 1/10

    # Calculate the length of the head
    head_length = snake_length * head_ratio

    # Calculate the length of the rest of the body
    body_length = snake_length - head_length

    # Subtract the head length from the body length to get the length of the body minus the head
    result = body_length - head_length
    return result

print(solution())