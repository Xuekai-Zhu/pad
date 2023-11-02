def solution():
    
    total_people = 5 * 12
    cans_per_person = 2
    cans_per_box = 10
    boxes_needed = total_people * cans_per_person / cans_per_box
    cost_per_box = 2
    total_cost = boxes_needed * cost_per_box
    num_family_members = 6
    cost_per_member = total_cost / num_family_members
    result = cost_per_member
    return result

print(solution())