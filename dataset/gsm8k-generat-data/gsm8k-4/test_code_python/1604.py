def solution():
    """Mary and Mike are sharing a jar of paint. Mary paints a dragon using 3 square feet worth of paint.
    Mike paints a castle using 2 square feet more paint than Mary used on her dragon.
    They both then work together to paint the biggest sun possible. If there was originally enough
    paint in the jar to cover 13 square feet, how many square feet of paint can be used to paint the sun?"""
    # Define the amount of paint used by Mary and Mike
    paint_mary = 3
    paint_mike = paint_mary + 2

    # Calculate the total amount of paint used
    total_paint_used = paint_mary + paint_mike

    # Calculate the amount of paint left in the jar after painting the dragon and the castle
    paint_left = 13 - total_paint_used

    # Assume that the sun they want to paint is circular and calculate its area
    sun_radius = paint_left / 2
    sun_area = 3.14 * sun_radius * sun_radius

    # Return the result
    result = sun_area
    return result

print(solution())