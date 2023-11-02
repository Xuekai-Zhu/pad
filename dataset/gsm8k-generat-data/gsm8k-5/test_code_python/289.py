def solution():
    total_models = 301  # Jim has 301 model cars in total

    # Let's say Jim has x Chevys
    # Jim has 2x+3 Fords
    # Jim has 4(2x+3)=8x+12 Buicks
    # The total number of cars is x + 2x + 3 + 8x + 12 = 11x + 15
    # So 11x + 15 = 301
    # Solving for x, we get x = 26
    # Therefore, Jim has 8x+12=212 Buicks
    num_buicks = 8 * 26 + 12
    result = num_buicks
    return result

print(solution())