def solution():
    """A total of 42 baby sea turtles hatched and are headed to the ocean. One-third of them got swept to the sea by a wave. How many are still on the sand?"""
    total_turtles = 42
    swept_turtles = total_turtles / 3
    remaining_turtles = total_turtles - swept_turtles
    result = remaining_turtles
    return result

print(solution())