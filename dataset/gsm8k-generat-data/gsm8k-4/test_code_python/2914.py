def solution():
    """Leah bought 3 boxes of birdseed. When she went to put them away, she discovered that she already had 5 boxes in the pantry. Her parrot eats 100 grams of seeds each week and her cockatiel eats 50 grams of seeds in a week. If each box of birdseed contains 225 grams, for how many weeks can she feed her birds without going back to the store?"""
    # Define the number of boxes of birdseed Leah has
    total_boxes = 3 + 5

    # Calculate the total amount of birdseed in grams
    total_birdseed = total_boxes * 225

    # Calculate the amount of birdseed the parrot and cockatiel eat each week
    weekly_usage = 100 + 50

    # Calculate the number of weeks Leah can feed her birds without going back to the store
    weeks_of_supply = total_birdseed / weekly_usage

    result = int(weeks_of_supply)
    return result

print(solution())