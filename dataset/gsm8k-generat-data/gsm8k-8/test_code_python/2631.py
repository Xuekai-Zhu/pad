def solution():
    # Calculate the yards of fabric needed for 3 shirts
    shirt_yards = 3 * 2

    # Calculate the yards of fabric needed for 5 pairs of pants
    pant_yards = 5 * 5

    # Calculate the total yards of fabric needed every day
    total_yards = shirt_yards + pant_yards

    # Calculate the total yards of fabric needed every 3 days
    total_yards_3_days = total_yards * 3
    result = total_yards_3_days
    return result

print(solution())