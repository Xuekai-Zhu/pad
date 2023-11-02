def solution():
    # Let's assume the first number is x, then the second number is twice that, or 2x
    x = 0
    while True:
        if x + 2*x == 33:
            result = 2*x
            break
        x += 1
    return result

print(solution())