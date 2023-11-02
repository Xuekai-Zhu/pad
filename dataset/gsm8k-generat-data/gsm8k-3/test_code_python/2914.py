def solution():
    """Leah bought 3 boxes of birdseed. When she went to put them away, she discovered that she already had 5 boxes in the pantry. Her parrot eats 100 grams of seeds each week and her cockatiel eats 50 grams of seeds in a week. If each box of birdseed contains 225 grams, for how many weeks can she feed her birds without going back to the store?"""
    # Define the amount of birdseed Leah has
    birdseed = (3 + 5) * 225  # 8 boxes total

    # Define the amount of seed each bird eats per week
    parrot_seed = 100
    cockatiel_seed = 50

    # Calculate the total amount of seed the birds eat per week
    total_seed = parrot_seed + cockatiel_seed

    # Calculate the number of weeks Leah can feed her birds with the amount of birdseed she has
    weeks = birdseed / total_seed

    # Display the number of weeks
    result = weeks
    return result

print(solution())