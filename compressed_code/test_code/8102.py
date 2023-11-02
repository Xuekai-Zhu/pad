def solution():
    
    total_boxes = 3 + 5
    total_seed = total_boxes * 225
    weekly_seed_needed = 100 + 50
    weeks_feedable = total_seed / weekly_seed_needed
    result = weeks_feedable
    return result

print(solution())