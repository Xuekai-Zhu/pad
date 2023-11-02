def solution():
    """John paints a giant mural that is 6m by 3m. The paint costs $4 per square meter. The artist can paint 1.5 square meters per hour and charges $10 per hour. How much does the mural cost?"""
    mural_width = 6
    mural_height = 3
    mural_area = mural_width * mural_height
    paint_cost_per_sq_meter = 4
    paint_cost = mural_area * paint_cost_per_sq_meter
    painting_speed = 1.5
    painting_rate = painting_speed * 10
    painting_time = mural_area / painting_rate
    labor_cost = painting_time * 10
    total_cost = paint_cost + labor_cost
    result = total_cost
    return result

print(solution())