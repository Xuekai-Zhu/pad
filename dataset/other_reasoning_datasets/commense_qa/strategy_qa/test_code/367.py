def solution():
    fibonacci_sequence = [0, 1]
    while len(str(fibonacci_sequence[-1])) < 2700000000000:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    pi_digits = 2700000000000
    if len(fibonacci_sequence) > pi_digits:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())