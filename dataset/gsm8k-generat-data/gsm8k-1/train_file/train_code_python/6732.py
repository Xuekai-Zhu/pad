def solution():
    """Tommy has a flag that is 5 feet wide and 4 feet tall. He wants to paint it with a new design. He knows from experience that he needs to paint both sides. Paint costs $2 a quart and a quart is good for 4 square feet. How much does he spend on paint?"""
    width = 5
    height = 4
    area = width * height * 2
    paint_needed = area / 4
    cost_per_quart = 2
    total_cost = paint_needed * cost_per_quart
    result = total_cost
    return result

print(solution())