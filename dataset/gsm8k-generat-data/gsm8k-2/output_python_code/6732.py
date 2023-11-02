def solution():
    """Tommy has a flag that is 5 feet wide and 4 feet tall. He wants to paint it with a new design. He knows from experience that he needs to paint both sides. Paint costs $2 a quart and a quart is good for 4 square feet. How much does he spend on paint?"""
    flag_area = 2 * 5 * 4
    paint_coverage_per_quart = 4
    paint_cost_per_quart = 2
    paint_needed = flag_area / paint_coverage_per_quart
    total_paint_cost = paint_needed * paint_cost_per_quart
    result = total_paint_cost
    return result

print(solution())