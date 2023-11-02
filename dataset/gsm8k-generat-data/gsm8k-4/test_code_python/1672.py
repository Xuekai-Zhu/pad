def solution():
    """In two years, Ophelia will be four times as old as Lennon. If Lennon is currently eight years old, how old is Ophelia?"""
    # Set up the equation using algebra: Ophelia's age in 2 years = 4 times Lennon's age in 2 years
    # Let x be Ophelia's current age
    # Let y be Lennon's current age (8 years old)
    # Therefore, (x+2) = 4(y+2)

    # Simplify the equation: x+2 = 4y+8
    # x = 4y+6

    # Substitute y = 8 into the equation to solve for x
    x = 4*8 + 6

    # Ophelia is currently x years old
    result = x
    return result

print(solution())