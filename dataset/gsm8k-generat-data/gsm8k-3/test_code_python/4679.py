def solution():
    """A total of 42 baby sea turtles hatched and are headed to the ocean. One-third of them got swept to the sea by a wave.  How many are still on the sand?"""
    # Find the number of turtles swept to sea
    swept_turtles = 42 // 3

    # Find the number of turtles still on the sand
    remaining_turtles = 42 - swept_turtles

    # Display the number of turtles on the sand
    result = remaining_turtles
    return result

print(solution())