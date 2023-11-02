def solution():
    
    seed_per_box = 225
    total_boxes = 3 + 5
    total_seed = total_boxes * seed_per_box
    parrot_seed_per_week = 100
    cockatiel_seed_per_week = 50
    total_seed_per_week = parrot_seed_per_week + cockatiel_seed_per_week
    weeks_of_seed = total_seed / total_seed_per_week
    result = weeks_of_seed
    return result

print(solution())