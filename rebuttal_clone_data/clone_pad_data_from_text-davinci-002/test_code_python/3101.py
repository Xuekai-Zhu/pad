def solution():
    gallons_sold = 180
    gallons_per_box = 30
    boxes_needed = math.ceil(gallons_sold / gallons_per_box)
    cost_per_box = 40
    total_cost = boxes_needed * cost_per_box
    result = total_cost
    
    return result

print(solution())