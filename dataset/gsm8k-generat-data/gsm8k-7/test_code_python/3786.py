def solution():
    current_length = 14
    required_length = 23
    final_length = 12

    # Calculate the amount of hair she needs to grow
    remaining_length = required_length - final_length

    # Add the remaining length to her current length
    total_length = current_length + remaining_length

    # Calculate the amount of additional length she needs to grow
    additional_length = total_length - current_length

    result = additional_length
    return result

print(solution())