def solution():
    rows_planted = 4
    corn_per_row = 70
    seeds_per_bag = 48
    seeds_per_ear = 2
    total_seeds = rows_planted * corn_per_row * seeds_per_ear
    seed_bags_per_kid = total_seeds / seeds_per_bag
    return seed_bags_per_kid

print(solution())