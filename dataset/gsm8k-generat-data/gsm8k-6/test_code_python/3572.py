def solution():
    # Calculate the number of blouses and dresses Eliza can iron in the given durations
    blouses = 2*60 // 15  # Eliza spends 2 hours (2 x 60 minutes) on blouses and can iron a blouse in 15 minutes
    dresses = 3*60 // 20  # Eliza spends 3 hours (3 x 60 minutes) on dresses and can iron a dress in 20 minutes

    # Calculate the total number of clothes Eliza ironed
    total_clothes = blouses + dresses
    result = total_clothes
    return result

print(solution())