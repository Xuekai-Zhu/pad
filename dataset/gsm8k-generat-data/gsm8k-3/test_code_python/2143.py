def solution():
    """The long jump finals contained four national champions competing against one another.  The first competitor jumped a distance of 22 feet.  The second competitor jumped one foot farther than the first competitor.  The third competitor jumped two feet shorter than the third competitor.  And the fourth competitor jumped 3 feet further than the third competitor.  How long, in feet, did the fourth competitor jump?"""
    # Define the distance jumped by the first competitor
    jump1 = 22

    # Calculate the distance jumped by the second competitor
    jump2 = jump1 + 1

    # Calculate the distance jumped by the third competitor
    jump3 = jump2 - 2

    # Calculate the distance jumped by the fourth competitor
    jump4 = jump3 + 3

    # Display the distance jumped by the fourth competitor
    result = jump4
    return result

print(solution())