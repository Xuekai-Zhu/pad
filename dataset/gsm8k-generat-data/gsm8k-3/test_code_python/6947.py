def solution():
    """In the garden, the gecko eats 12 bugs.  The lizard eats half as many bugs as the gecko.  The frog eats 3 times as many bugs as the lizard.  The toad eats 50% more bugs than the frog. How many bugs are eaten in total by all of them?"""
    # Number of bugs eaten by the gecko
    gecko = 12

    # Number of bugs eaten by the lizard
    lizard = gecko / 2

    # Number of bugs eaten by the frog
    frog = lizard * 3

    # Number of bugs eaten by the toad
    toad = frog * 1.5

    # Total number of bugs eaten
    total_bugs = gecko + lizard + frog + toad

    # Display the total number of bugs eaten
    result = total_bugs
    return result

print(solution())