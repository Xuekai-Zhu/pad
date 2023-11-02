def solution():
    original_length = 20
    percent_shortened = 0.3

    # Calculate the length after being shortened
    shortened_length = original_length * (1 - percent_shortened)

    result = shortened_length
    return result

print(solution())