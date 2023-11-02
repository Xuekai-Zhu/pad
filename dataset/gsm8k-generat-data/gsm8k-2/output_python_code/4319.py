def solution():
    """John paints a giant mural that is 6m by 3m. The paint costs $4 per square meter. The artist can paint 1.5 square meters per hour and charges $10 per hour. How much does the mural cost?"""
    mural_area = 6 * 3
    paint_cost_per_sqm = 4
    paint_cost = mural_area * paint_cost_per_sqm
    painting_speed = 1.5
    painting_time = mural_area / painting_speed
    painting_cost_per_hour = 10
    painting_cost = painting_time * painting_cost_per_hour
    total_cost = paint_cost + painting_cost
    result = total_cost
    return result

print(solution())