def solution():
    # Calculate the perimeter of the rectangle
    perimeter = 2*28 + 2*x  # Let x be the length of each shorter side
    
    # Set up an equation using the perimeter and total length of rope
    2*28 + 2*x = 100
    
    # Solve for x
    x = (100 - 2*28) / 2
    
    result = x
    return result

print(solution())