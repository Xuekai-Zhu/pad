def solution():
    total_legs = 20  # Total number of legs in the flock
    legs_per_tripodasaurus = 3  # Each tripodasaurus has 3 legs

    # Calculate the number of tripodasauruses in the flock
    num_tripodasauruses = total_legs // legs_per_tripodasaurus
    result = num_tripodasauruses
    return result

print(solution())