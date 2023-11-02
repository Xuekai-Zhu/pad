def solution():
    """The total average age of three friends is 40. Jared is ten years older than Hakimi, and Molly's age is 30. How old is Hakimi?"""
    # Let H be Hakimi's age
    # Jared is 10 years older than Hakimi, so J = H + 10
    # The total average age of the three friends is 40, so (H + J + 30) / 3 = 40
    # Simplifying the equation, we get: H + J + 30 = 120
    # Substituting J with H + 10, we get: H + H + 10 + 30 = 120
    # Simplifying the equation, we get: 2H + 40 = 120
    # Solving for H, we get: H = 40 - 20 = 20

    # Therefore, Hakimi is 20 years old.
    result = 20
    return result

print(solution())