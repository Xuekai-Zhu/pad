def solution():
    """Jake and Penny are hunting snakes. Jake's snake is 12 inches longer than Jenny's snake. If the two snakes have a combined length of 70 inches, how long is Jake's snake?"""
    # Let x be the length of Jenny's snake
    # Jake's snake is 12 inches longer, so its length is x + 12
    # The sum of their lengths is 70, so x + (x+12) = 70
    # Simplifying the equation gives 2x + 12 = 70
    # Solving for x gives x = 29
    # Therefore, Jake's snake is x+12 = 41 inches long

    jennys_snake_length = 29
    jakes_snake_length = jennys_snake_length + 12
    result = jakes_snake_length
    return result

print(solution())