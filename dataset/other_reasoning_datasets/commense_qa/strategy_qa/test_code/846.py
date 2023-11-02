def solution():
    fibonacci_sequence = [1, 1, 2, 3, 5, 8]
    single_digit_fibonacci = []
    # Loop through the Fibonacci sequence and add single digit numbers to a list
    for num in fibonacci_sequence:
        if num < 10:
            if num not in single_digit_fibonacci:
                single_digit_fibonacci.append(num)
    # Check if there are five different single-digit Fibonacci numbers
    if len(single_digit_fibonacci) == 5:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())