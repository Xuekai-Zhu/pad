def solution():
    height = 60
    leg_ratio = 1 / 3
    head_ratio = 1 / 4

    # Calculate the length of Miss Aisha's legs
    leg_length = height * leg_ratio

    # Calculate the length of Miss Aisha's head
    head_length = height * head_ratio

    # Calculate the length of the rest of Miss Aisha's body
    rest_of_body_length = height - leg_length - head_length
    result = rest_of_body_length
    return result

print(solution())