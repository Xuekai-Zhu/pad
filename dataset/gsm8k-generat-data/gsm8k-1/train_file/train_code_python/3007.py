def solution():
    """A snake's head is one-tenth its length. If a snake is 10 feet long, calculate the length of the rest of its body minus the head."""
    snake_length = 10
    head_length = snake_length / 10
    body_length = snake_length - head_length
    result = body_length - head_length
    return result

print(solution())