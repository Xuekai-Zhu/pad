def solution():
    
    total_people = 5 * 12
    cans_per_person = 2
    total_cans_needed = total_people * cans_per_person
    cans_per_box = 10
    cost_per_box = 2
    boxes_needed = total_cans_needed / cans_per_box
    cost_per_family = boxes_needed * cost_per_box
    cost_per_member = cost_per_family / 6
    result = cost_per_member
    return result

print(solution())