def solution():
    
    males = 15
    girls = males + 10
    total_attendees = males + girls
    cans_needed = total_attendees * 2
    boxes_needed = cans_needed // 8 + (cans_needed % 8 > 0)
    price_per_box = 5
    total_cost = boxes_needed * price_per_box
    result = total_cost
    return result

print(solution())