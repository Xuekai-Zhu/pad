def solution():
    emergency_number = 999
    # List the first few Fibonacci number to check if the emergency number is Fibonacci
    fib_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
    if emergency_number in fib_sequence:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())