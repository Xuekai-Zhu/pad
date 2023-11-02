def solution():
    """Leah bought 3 boxes of birdseed. When she went to put them away, she discovered that she already had 5 boxes in the pantry. Her parrot eats 100 grams of seeds each week and her cockatiel eats 50 grams of seeds in a week. If each box of birdseed contains 225 grams, for how many weeks can she feed her birds without going back to the store?"""
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