def solution():

    total_patches = 16 * 20
    first_ten_patches = 10
    patch_price = 10
    remaining_patches = total_patches - first_ten_patches
    patch_price_decrease = patch_price / 2
    total_patch_price = (first_ten_patches * patch_price) + (remaining_patches * patch_price_decrease)
    result = total_patch_price

    return result

print(solution())