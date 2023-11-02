def solution():
    """A total of 42 baby sea turtles hatched and are headed to the ocean. One-third of them got swept to the sea by a wave. How many are still on the sand?"""
    # Define the initial number of baby sea turtles
    initial_turtles = 42

    # Calculate the number of baby sea turtles that got swept to the sea
    swept_turtles = initial_turtles // 3

    # Calculate the number of baby sea turtles still on the sand
    turtles_on_sand = initial_turtles - swept_turtles

    # Return the result
    result = turtles_on_sand
    return result

print(solution())