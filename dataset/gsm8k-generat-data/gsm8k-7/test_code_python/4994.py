def solution():
    combined_age = 132

    # Let's assign the age of Jeremy as 'x'
    x = None

    # Amy's age is 1/3 of Jeremy's age, so we can express her age as x/3
    amy_age = x / 3

    # Chris is twice as old as Amy, so we can express his age as 2 * Amy's age or 2 * (x/3)
    chris_age = 2 * (x/3)

    # Now we can express the combined age of all three as the sum of their individual ages
    total_age = x + amy_age + chris_age

    # We can set up an equation to solve for the unknown value of 'x', which is Jeremy's age
    # combined_age = x + amy_age + chris_age
    # combined_age = x + (x/3) + 2 * (x/3)
    # combined_age = 3 * (x/3) + (x/3) + (2 * x/3)
    # combined_age = 4 * (x/3) --> multiply both sides by 3/4
    # (3/4) * combined_age = x
    x = (3/4) * combined_age

    result = x
    return result

print(solution())