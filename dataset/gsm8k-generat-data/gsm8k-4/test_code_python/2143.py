def solution():
    """The long jump finals contained four national champions competing against one another. The first competitor jumped a distance of 22 feet. The second competitor jumped one foot farther than the first competitor. The third competitor jumped two feet shorter than the third competitor. And the fourth competitor jumped 3 feet further than the third competitor. How long, in feet, did the fourth competitor jump?"""
    # Define the initial distance jumped by the first competitor
    first_distance = 22

    # Calculate the second distance
    second_distance = first_distance + 1

    # Calculate the third distance
    third_distance = second_distance - 2

    # Calculate the fourth distance
    fourth_distance = third_distance + 3

    # return the result
    result = fourth_distance
    return result

print(solution())