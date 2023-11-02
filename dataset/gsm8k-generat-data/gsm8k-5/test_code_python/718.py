def solution():
    combined_length = 70  # The two snakes have a combined length of 70 inches

    # Let x be the length of Jenny's snake
    # Then Jake's snake is x + 12 inches long
    # And x + (x + 12) = 70
    # Solving for x gives x = 29
    # Therefore, Jake's snake is x + 12 = 41 inches long

    jenny_length = 29
    jake_length = jenny_length + 12
    result = jake_length
    return result

print(solution())