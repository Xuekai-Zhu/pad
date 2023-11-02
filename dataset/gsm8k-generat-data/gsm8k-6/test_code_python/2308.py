def solution():
    # Calculate the total number of bandages used by Peggy
    total_bandages_used = 2 + 3  # Peggy used two bandages on her left knee and three bandages on her right knee

    # Calculate the total number of bandages in the box before Peggy used them
    total_bandages_in_box = 2 * 12 - 8  # the box had 8 less than 2 dozen bandages, which is 2 * 12 - 8 = 16

    # Calculate the number of bandages left in the box after Peggy used them
    bandages_left = total_bandages_in_box - total_bandages_used
    result = bandages_left
    return result

print(solution())