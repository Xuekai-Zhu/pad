def solution():
    """Frederick is making popsicles to sell and to save money he is making his own popsicle sticks. He can get 200 sticks from a 2 x 4 piece of wood and 400 sticks from a 2 x 8 piece of wood. He has $24 to buy wood for sticks. A 2 x 4 costs $4. A 2 x 8 costs $6. What is the most popsicle sticks he can make if he buys the cheapest lumber?"""
    cost_2x4 = 4
    cost_2x8 = 6
    budget = 24

    # Calculate maximum number of 2x4s that can be bought
    max_2x4 = budget // cost_2x4

    # Calculate maximum number of 2x8s that can be bought
    max_2x8 = budget // cost_2x8

    # Calculate maximum number of popsicle sticks that can be made from buying 2x4s
    sticks_from_2x4 = max_2x4 * 200

    # Calculate maximum number of popsicle sticks that can be made from buying 2x8s
    sticks_from_2x8 = max_2x8 * 400

    # Determine which lumber to buy based on which one results in the most popsicle sticks
    if sticks_from_2x4 > sticks_from_2x8:
        max_sticks = sticks_from_2x4
    else:
        max_sticks = sticks_from_2x8

    result = max_sticks
    return result

print(solution())