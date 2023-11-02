def solution():
    """Martha needs to paint all four walls in her 12 foot by 16 foot kitchen, which has 10 foot high ceilings. Each wall needs one coat of primer and two coats of paint. If Martha can paint 40 square feet per hour, how many hours will it take her to paint the kitchen?"""
    # Calculate the total surface area of the walls to be painted
    wall_area = 2 * (12 * 10) + 2 * (16 * 10)
    total_area = wall_area * 3

    # Calculate the number of hours needed to complete the job
    hours = total_area / 40

    # Display the number of hours needed to complete the job
    result = hours
    return result

print(solution())