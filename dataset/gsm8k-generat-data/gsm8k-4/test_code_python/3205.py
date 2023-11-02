def solution():
    """Jason's dog has a tail that's half the length of its body, and a head that's 1/6 the length of its body. If the dog is 30 inches long overall, how long is its tail?"""
    # Define the total length of the dog and the proportion of its body that is the tail and head
    total_length = 30
    tail_proportion = 0.5
    head_proportion = 1/6

    # Calculate the length of the body
    body_length = total_length / (tail_proportion + head_proportion + 1)

    # Calculate the length of the tail
    tail_length = body_length * tail_proportion

    # return the result
    result = tail_length
    return result

print(solution())