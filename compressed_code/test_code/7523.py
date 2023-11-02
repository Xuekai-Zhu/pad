def solution():
    
    males = 15
    girls = males + 10
    total_attendees = males + girls
    cans_per_attendee = 2
    total_cans = total_attendees * cans_per_attendee
    cans_per_box = 8
    boxes_needed = total_cans // cans_per_box + (total_cans % cans_per_box > 0)
    cost_per_box = 5
    total_cost = boxes_needed * cost_per_box
    result = total_cost
    return result

print(solution())