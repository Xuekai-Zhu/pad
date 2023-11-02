def solution():
    """Martha needs to paint all four walls in her 12 foot by 16 foot kitchen, which has 10 foot high ceilings. Each wall needs one coat of primer and two coats of paint. If Martha can paint 40 square feet per hour, how many hours will it take her to paint the kitchen?"""
    # Define the dimensions of the kitchen
    kitchen_length = 16
    kitchen_width = 12
    kitchen_height = 10

    # Calculate the area of the walls
    wall_area = 2 * (kitchen_length * kitchen_height + kitchen_width * kitchen_height)

    # Calculate the total area that needs to be painted (one coat of primer and two coats of paint)
    total_area = 3 * wall_area

    # Calculate the number of hours needed to paint the kitchen
    hours = total_area / 40

    # Round up to the nearest hour
    hours = round(hours + 0.5)

    # Return the result
    result = hours
    return result

print(solution())