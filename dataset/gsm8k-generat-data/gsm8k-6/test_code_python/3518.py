def solution():
    # Find the total area of the four walls
    wall_area = 2 * (10 * 12) + 2 * (10 * 16)
    
    # Find the total area to be painted (one coat of primer and two coats of paint)
    total_paint_area = wall_area * 3

    # Calculate the number of hours it will take Martha to paint the kitchen
    hours_to_paint = total_paint_area / 40  # Martha can paint 40 square feet per hour
    
    result = hours_to_paint
    return result

print(solution())