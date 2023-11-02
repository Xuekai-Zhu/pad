def solution():
    # Define the number of levels and legos per side for the bottom level
    levels = 3
    legos_per_side = 7

    # Use a loop to calculate the total number of legos needed for all levels
    total_legos = 0
    for i in range(levels):
        legos_on_level = legos_per_side ** 2
        total_legos += legos_on_level
        legos_per_side -= 1

    result = total_legos
    return result

print(solution())