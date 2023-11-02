def solution():
    # Convert a gallon to liters
    gallon_to_liter = 4  
    
    # Calculate the total amount of paint used by Dexter and Jay
    total_paint_used = (3/8 + 5/8) * gallon_to_liter  
    
    # Calculate the amount of paint left
    paint_left = gallon_to_liter - total_paint_used 
    result = paint_left
    return result

print(solution())