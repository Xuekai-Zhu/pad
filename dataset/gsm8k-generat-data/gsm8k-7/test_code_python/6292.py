def solution():
    # Let x be the present age of Allen's mother
    # Then Allen's present age is x - 25
    # In 3 years, their ages will be x + 3 and x - 22
    # The sum of their ages in 3 years will be (x + 3) + (x - 22) = 2x - 19
    # We know that the sum of their ages in 3 years is 41, so we have:
    2x - 19 = 41

    # Solving for x, we get:
    x = (41 + 19) / 2
    x = 30

    # Therefore, Allen's mother is currently 30 years old
    result = x
    return result

print(solution())