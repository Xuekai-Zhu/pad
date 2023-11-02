def solution():
    """Leah bought 3 boxes of birdseed. When she went to put them away, she discovered that she already had 5 boxes in the pantry. Her parrot eats 100 grams of seeds each week and her cockatiel eats 50 grams of seeds in a week. If each box of birdseed contains 225 grams, for how many weeks can she feed her birds without going back to the store?"""
    total_boxes = 3 + 5
    total_seed = total_boxes * 225
    weekly_seed_needed = 100 + 50
    weeks_feedable = total_seed / weekly_seed_needed
    result = weeks_feedable
    return result

print(solution())