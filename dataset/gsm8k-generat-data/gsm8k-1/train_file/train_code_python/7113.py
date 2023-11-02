def solution():
    """John buys 3 barbells and gives $850 and gets $40 in change. How much did each barbell cost?"""
    total_cost = 850 - 40
    num_barbells = 3
    cost_per_barbell = total_cost / num_barbells
    result = cost_per_barbell
    return result

print(solution())