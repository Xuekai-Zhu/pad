def solution():
    """Jason's dog has a tail that's half the length of its body, and a head that's 1/6 the length of its body. If the dog is 30 inches long overall, how long is its tail?"""
    total_length = 30
    body_length = total_length / (1 + 0.5 + 1/6)
    tail_length = body_length * 0.5
    result = tail_length
    return result

print(solution())