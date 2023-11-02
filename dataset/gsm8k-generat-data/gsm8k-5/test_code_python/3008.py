def solution():
    total_length = 10  # The snake is 10 feet long
    head_length = total_length / 10  # The head is one-tenth the length of the snake
    body_length = total_length - head_length  # Calculate the length of the rest of the snake's body
    result = body_length - head_length  # Subtract the length of the head from the body length
    return result

print(solution())