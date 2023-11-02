def solution():
    """Leonard is 4 years younger than Nina who is half as old as Jerome. If the sum of their ages is 36, what is Leonard's age?"""
    # Let's define Nina's age as n and Jerome's age as j
    # According to the problem, Leonard is 4 years younger than Nina
    l = n - 4
    # It is also given that Nina is half as old as Jerome
    n = j / 2
    # The sum of their ages is 36, so we can write an equation
    # j + n + l = 36
    # We can substitute n and l in terms of j into the equation
    j + j/2 + (j/2 - 4) = 36
    # Simplifying the equation
    2.5j - 8 = 36
    2.5j = 44
    j = 17.6
    # Now that we know Jerome's age, we can find Nina's age and then Leonard's age
    n = j / 2
    l = n - 4
    # Display Leonard's age
    result = int(l)
    return result

print(solution())