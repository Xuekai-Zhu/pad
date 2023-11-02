def solution():
    
    A = 30
    B = 2 * A
    C = A + 10
    D = C - 5
    total_registered = A + B + C + D
    not_ABCD = 185 - total_registered
    result = not_ABCD
    return result

print(solution())