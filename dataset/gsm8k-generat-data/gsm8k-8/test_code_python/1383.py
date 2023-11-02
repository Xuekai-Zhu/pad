def solution():
    # Define the total number of writing utensils and the ratio of pencils to pens
    total_utensils = 108
    pen_to_pencil_ratio = 1/5

    # Set up equations
    # Let x be the number of pens and y be the number of pencils
    # x + y = total_utensils
    # y = pen_to_pencil_ratio * x + 12
    # Solve for x
    x = (total_utensils - 12) / (1 + pen_to_pencil_ratio)
    
    result = x
    return result

print(solution())