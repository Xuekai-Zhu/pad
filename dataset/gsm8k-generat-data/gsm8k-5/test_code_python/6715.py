def solution():
    # Christine's first throw
    christine_first = 20

    # Janice's first throw
    janice_first = christine_first - 4

    # Christine's second throw
    christine_second = christine_first + 10

    # Janice's second throw
    janice_second = janice_first * 2

    # Christine's final throw
    christine_final = christine_second + 4

    # Janice's final throw
    janice_final = christine_first + 17

    # Find the highest throw
    highest_throw = max(christine_first, janice_first, christine_second, janice_second, christine_final, janice_final)
    result = highest_throw
    return result

print(solution())