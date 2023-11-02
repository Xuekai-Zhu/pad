def solution():
    # Define the length of the dog's body and head, and the total length of the dog
    total_length = 30
    body_length = total_length * (2/3)
    head_length = total_length * (1/6)

    # Calculate the length of the dog's tail
    tail_length = body_length * (1/2)

    result = tail_length
    return result

print(solution())