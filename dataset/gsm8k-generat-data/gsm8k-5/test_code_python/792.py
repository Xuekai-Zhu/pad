def solution():
    total_floors = 35  # The two buildings together have 35 floors
    # Let x be the number of floors in the Leeward Center
    # Then the number of floors in the Chrysler Building is x + 11
    # We know that x + (x + 11) = 35, so we can solve for x
    x = (35 - 11) / 2
    # The number of floors in the Chrysler Building is x + 11
    chrysler_floors = x + 11
    result = chrysler_floors
    return result

print(solution())