def solution():
    total_legos = 500  # James starts with 500 Legos
    used_legos = total_legos / 2  # James uses half the Legos
    remaining_legos = total_legos - used_legos  # James has this many Legos left
    missing_legos = 5  # James can't find 5 Legos

    # Calculate the number of Legos in the box at the end
    legos_in_box = remaining_legos - missing_legos
    result = legos_in_box
    return result

print(solution())