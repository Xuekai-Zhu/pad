def solution():
    total_length = 30
    body_length = total_length / (1 + 1/2 + 1/6) # Calculate body length using proportions
    tail_length = body_length / 2 # Tail length is half the body length
    result = tail_length
    return result

print(solution())