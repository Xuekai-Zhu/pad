def solution():
    total_rings = 52
    ratio_small_big = 4 + 1/3

    # Calculate the total number of times Martin rings the small bell
    total_small_rings = total_rings / (ratio_small_big + 1)

    # Calculate the total number of times Martin rings the big bell
    total_big_rings = total_small_rings * ratio_small_big
    result = total_big_rings
    return result

print(solution())