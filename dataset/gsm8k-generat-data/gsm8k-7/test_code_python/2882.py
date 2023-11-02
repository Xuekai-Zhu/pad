def solution():
    gallon_paint = 1
    dexter_used = 3/8
    jay_used = 5/8
    gallon_to_liters = 4

    total_used = dexter_used + jay_used

    # Calculate the remaining paint in gallons
    remaining_paint_gallons = gallon_paint - total_used
    
    # Convert remaining paint from gallons to liters
    remaining_paint_liters = remaining_paint_gallons * gallon_to_liters
    result = remaining_paint_liters
    return result

print(solution())