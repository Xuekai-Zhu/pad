def solution():
    """James wants to build a 16-foot by 20-foot quilt. He uses patches that are each 4 square feet. The first 10 patches cost $10 each and then each patch after that cost half as much. How much do the patches for the quilt cost?"""
    quilt_width = 16
    quilt_length = 20
    patch_size = 4
    total_patch_size = quilt_width * quilt_length / patch_size
    first_10_patch_cost = 10 * 10
    remaining_patch_cost = (total_patch_size - 10) * 5
    total_patch_cost = first_10_patch_cost + remaining_patch_cost
    result = total_patch_cost
    return result

print(solution())