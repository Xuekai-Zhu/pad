def solution():
    # Define Jonny's number of stairs climbed
    jonny_stairs = 1269

    # Calculate Julia's number of stairs climbed
    julia_stairs = (1/3) * jonny_stairs - 7

    # Calculate the total number of stairs climbed
    total_stairs = jonny_stairs + julia_stairs

    result = total_stairs
    return result

print(solution())