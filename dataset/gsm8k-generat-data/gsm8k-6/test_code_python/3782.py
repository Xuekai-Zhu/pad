def solution():
    # Initialize variables
    sand_dollars = 10
    glass_pieces = 3 * sand_dollars
    seashells = 5 * glass_pieces

    # Calculate total number of treasures
    total_treasures = sand_dollars + glass_pieces + seashells
    result = total_treasures
    return result

print(solution())