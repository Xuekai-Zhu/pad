def solution():
    
    
    pencils_per_box = 80
    num_boxes = 15
    total_pencils_ordered = pencils_per_box * num_boxes

    
    pens_ordered = (2 * total_pencils_ordered) + 300

    
    cost_of_pencils = total_pencils_ordered * 4
    cost_of_pens = pens_ordered * 5
    total_cost = cost_of_pencils + cost_of_pens

    result = total_cost
    return result

print(solution())