def solution():
    """James wants to build a 16-foot by 20-foot quilt. He uses patches that are each 4 square feet. The first 10 patches cost $10 each and then each patch after that cost half as much. How much do the patches for the quilt cost?"""
    quilt_area = 16 * 20
    patch_area = 4
    total_patches = quilt_area / patch_area
    first_10_patches_cost = 10 * 10
    remaining_patches = total_patches - 10
    remaining_patches_cost = 0
    if remaining_patches > 0:
        for i in range(0, remaining_patches):
            remaining_patches_cost += ((10 / 2) ** i) * 10
    total_cost = first_10_patches_cost + remaining_patches_cost
    result = total_cost
    return result

print(solution())