def solution():
    # Let's assume Leonard's age to be x
    x = 0

    # Since Nina is half as old as Jerome, let's assume Jerome's age to be y
    y = 2 * 36 / 3

    # From the given conditions, we know that Leonard is 4 years younger than Nina
    # So, Nina's age can be represented as x + 4
    # And we know that the sum of their ages is 36
    # Therefore, we can write the equation: x + (x + 4) + y = 36
    # Simplifying this equation, we get:
    x = (36 - y - 4) / 2

    result = x
    return result

print(solution())