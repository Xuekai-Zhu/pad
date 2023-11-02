def solution():
    total_length = 30  # The dog is 30 inches long overall
    body_length = total_length - (total_length * (1/6) + total_length * (1/2))  # Calculate the length of the body
    tail_length = body_length / 2  # The tail is half the length of the body

    result = tail_length
    return result

print(solution())