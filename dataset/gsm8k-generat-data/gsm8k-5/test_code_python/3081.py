def solution():
    pea_patch_area = 2 * 5 * 6  # The pea patch is twice the size of the radish patch, and 1/6th of it is 5 square feet
    radish_patch_area = pea_patch_area / 2  # The radish patch is half the size of the pea patch

    result = radish_patch_area
    return result

print(solution())