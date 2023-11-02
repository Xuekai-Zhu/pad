def solution():
    # Calculate the total number of slices of pizza
    total_slices = 2 * 12  # 2 large pizzas, each cut into 12 slices
    
    # Calculate the number of slices left after Dean and his friends had their share
    remaining_slices = total_slices - (6 + 3 + (1/3)*12)  # Dean ate half of 1 pizza (6 slices), Frank ate 3 slices, Sammy ate 1/3 of 1 pizza (4 slices)
    result = remaining_slices
    return result

print(solution())