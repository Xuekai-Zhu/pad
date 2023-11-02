def solution():
    """In the garden, the gecko eats 12 bugs. The lizard eats half as many bugs as the gecko. The frog eats 3 times as many bugs as the lizard. The toad eats 50% more bugs than the frog. How many bugs are eaten in total by all of them?"""
    # Define the number of bugs eaten by the gecko
    gecko_bugs = 12

    # Calculate the number of bugs eaten by the lizard
    lizard_bugs = gecko_bugs / 2

    # Calculate the number of bugs eaten by the frog
    frog_bugs = lizard_bugs * 3

    # Calculate the number of bugs eaten by the toad
    toad_bugs = frog_bugs * 1.5

    # Calculate the total number of bugs eaten
    total_bugs = gecko_bugs + lizard_bugs + frog_bugs + toad_bugs

    result = total_bugs
    return result

print(solution())