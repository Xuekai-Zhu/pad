def solution():
    # Define the total number of Legos
    total_legos = 500

    # Calculate the number of Legos used in the castle
    castle_legos = total_legos / 2

    # Calculate the number of Legos left in the box
    remaining_legos = total_legos - castle_legos

    # Subtract the 5 missing Legos
    final_lego_count = remaining_legos - 5
    result = final_lego_count
    return result

print(solution())