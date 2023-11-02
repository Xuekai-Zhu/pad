def solution():
    """Jason's dog has a tail that's half the length of its body, and a head that's 1/6 the length of its body. If the dog is 30 inches long overall, how long is its tail?"""
    # Define the length of the dog's body
    body_length = 30

    # Calculate the length of the dog's tail
    tail_length = body_length / (1 + 2)

    # Display the length of the dog's tail
    result = tail_length
    return result

print(solution())