def solution():
    
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