def solution():
    
    darren_boxes = 4
    darren_crackers_per_box = 24
    darren_total_crackers = darren_boxes * darren_crackers_per_box
    calvin_boxes = 2 * darren_boxes - 1
    calvin_total_crackers = calvin_boxes * darren_crackers_per_box
    total_crackers = darren_total_crackers + calvin_total_crackers
    result = total_crackers
    return result

print(solution())