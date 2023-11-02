def solution():
    """Bob thinks he needs 56 popsicle sticks to recreate the Washington Monument for his history project. His favorite popsicles come 8 to a box and cost $2.00 per box. How much will it cost Bob to build his project?"""
    popsicles_per_box = 8
    popsicles_needed = 56
    boxes_needed = popsicles_needed / popsicles_per_box
    price_per_box = 2.00
    project_cost = boxes_needed * price_per_box
    result = project_cost
    return result

print(solution())