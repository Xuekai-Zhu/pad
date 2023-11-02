def solution():
    
    darren_boxes = 4
    darren_crackers = darren_boxes * 24
    calvin_boxes = 2 * darren_boxes - 1
    calvin_crackers = calvin_boxes * 24
    total_crackers = darren_crackers + calvin_crackers
    result = total_crackers
    return result

print(solution())