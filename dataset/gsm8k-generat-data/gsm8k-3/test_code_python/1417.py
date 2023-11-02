def solution():
    """The sum of Mario and Maria's ages now is 7. Mario is 1 year older than Maria. How old is Mario?"""
    # Let's assume that Maria's age is "x"
    # Since Mario is 1 year older than Maria, his age would be "x+1"
    # Then we know that the sum of their ages is 7, so we can write an equation:
    # x + (x+1) = 7
    # Solving for x, we get:
    x = (7 - 1) / 2
    # Therefore, Maria is 3 years old and Mario is 4 years old.
    result = x + 1
    return result

print(solution())