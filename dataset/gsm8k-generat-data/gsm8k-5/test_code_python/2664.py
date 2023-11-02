def solution():
    total_slices = 4 * 12  # There are 4 pizzas, each cut into 12 slices
    eaten_slices = 39  # The guests ate 39 slices of pizza

    # Calculate the remaining slices of pizza
    remaining_slices = total_slices - eaten_slices
    result = remaining_slices
    return result

print(solution())