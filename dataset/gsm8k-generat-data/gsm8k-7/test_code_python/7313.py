def solution():
    hats_per_yard = 4
    yards_per_cloak = 3

    num_cloaks = 6
    num_hats = 12

    # Calculate the total number of yards needed for hats
    total_hats_yards = num_hats / hats_per_yard

    # Calculate the total number of yards needed for cloaks
    total_cloaks_yards = num_cloaks * yards_per_cloak

    # Calculate the total yards needed for all items
    total_yards = total_hats_yards + total_cloaks_yards
    result = total_yards
    return result

print(solution())