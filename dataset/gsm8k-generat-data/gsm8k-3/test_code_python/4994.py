def solution():
    """Amy, Jeremy, and Chris have a combined age of 132.  Amy is 1/3 the age of Jeremy, and Chris is twice as old as Amy.  How old is Jeremy?"""
    # Let's assume Jeremy's age is x
    x = 0

    # Calculate Amy's age
    amy_age = x / 3

    # Calculate Chris's age
    chris_age = 2 * amy_age

    # Calculate the total age of all three people
    total_age = amy_age + x + chris_age

    # Set up an equation to solve for x
    x + amy_age + chris_age = 132

    # Solve for x
    x = (132 - chris_age) / 1.3333

    # Display Jeremy's age
    result = x
    return result

print(solution())