def solution():
    """A snake's head is one-tenth its length. If a snake is 10 feet long, calculate the length of the rest of its body minus the head."""
    # Define the length of the snake and the proportion of its head
    snake_length = 10
    head_proportion = 1/10

    # Calculate the length of the snake's head
    head_length = snake_length * head_proportion

    # Calculate the length of the rest of the snake's body
    body_length = snake_length - head_length

    # Calculate the length of the rest of the snake's body minus the head
    rest_of_body_length = body_length - head_length

    result = rest_of_body_length
    return result

print(solution())