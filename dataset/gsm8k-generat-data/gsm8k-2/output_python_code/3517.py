def solution():
    """Martha needs to paint all four walls in her 12 foot by 16 foot kitchen, which has 10 foot high ceilings. 
    Each wall needs one coat of primer and two coats of paint. If Martha can paint 40 square feet per hour, 
    how many hours will it take her to paint the kitchen?"""
    wall_area = 10 * 12 * 4 + 10 * 16 * 2
    total_area = wall_area * 3
    painting_speed = 40
    total_hours = total_area / painting_speed
    result = total_hours
    return result

print(solution())