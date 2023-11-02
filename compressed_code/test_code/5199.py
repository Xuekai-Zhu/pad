def solution():
    
    flag_area = 2 * 5 * 4
    paint_coverage_per_quart = 4
    paint_cost_per_quart = 2
    paint_needed = flag_area / paint_coverage_per_quart
    total_paint_cost = paint_needed * paint_cost_per_quart
    result = total_paint_cost
    return result

print(solution())