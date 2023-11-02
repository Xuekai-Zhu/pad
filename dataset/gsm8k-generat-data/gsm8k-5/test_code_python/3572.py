def solution():
    # Calculate the number of blouses Eliza can iron in 2 hours (120 minutes)
    blouses_per_hour = 60 / 15  # Eliza can iron 4 blouses per hour
    total_blouses = blouses_per_hour * 2  # Eliza can iron 8 blouses in 2 hours

    # Calculate the number of dresses Eliza can iron in 3 hours (180 minutes)
    dresses_per_hour = 60 / 20  # Eliza can iron 3 dresses per hour
    total_dresses = dresses_per_hour * 3  # Eliza can iron 9 dresses in 3 hours

    # Calculate the total number of pieces of clothes Eliza ironed
    total_pieces = total_blouses + total_dresses
    result = total_pieces
    return result

print(solution())