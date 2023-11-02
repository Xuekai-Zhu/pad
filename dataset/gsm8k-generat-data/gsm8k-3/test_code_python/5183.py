def solution():
    """Miss Aisha's legs are 1/3 of her total height. If her head is also 1/4 of her total height, and she is 60 inches tall, calculate the length of the rest of her body."""
    # Define the total height
    total_height = 60

    # Calculate the length of Miss Aisha's legs
    leg_length = total_height / 3

    # Calculate the length of Miss Aisha's head
    head_length = total_height / 4

    # Calculate the length of the rest of Miss Aisha's body
    body_length = total_height - leg_length - head_length

    # Display the length of the rest of Miss Aisha's body
    result = body_length
    return result

print(solution())