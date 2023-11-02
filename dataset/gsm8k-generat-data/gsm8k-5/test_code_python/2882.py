def solution():
    total_paint = 1  # A gallon of white paint is being used
    dexter_paint = 3/8 * total_paint  # Dexter used 3/8 of the paint
    jay_paint = 5/8 * total_paint  # Jay used 5/8 of the paint
    total_used_paint = dexter_paint + jay_paint  # Total paint used by Dexter and Jay
    remaining_paint = total_paint - total_used_paint  # Paint left after Dexter and Jay are done

    # Convert remaining paint from gallons to liters
    remaining_paint_liters = remaining_paint * 4
    result = remaining_paint_liters
    return result

print(solution())