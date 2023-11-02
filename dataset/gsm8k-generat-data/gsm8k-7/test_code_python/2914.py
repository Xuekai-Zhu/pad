def solution():
    num_boxes_bought = 3
    num_boxes_already = 5
    num_boxes_total = num_boxes_bought + num_boxes_already
    seed_per_week_parrot = 100
    seed_per_week_cockatiel = 50
    grams_per_box = 225

    # Calculate the total amount of birdseed in grams
    total_seed = num_boxes_total * grams_per_box

    # Calculate the amount of seed used per week
    total_seed_per_week = seed_per_week_cockatiel + seed_per_week_parrot

    # Calculate the number of weeks she can feed her birds
    num_weeks = total_seed / total_seed_per_week
    result = num_weeks
    return result

print(solution())