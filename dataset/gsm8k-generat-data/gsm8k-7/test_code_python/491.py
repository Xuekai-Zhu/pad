def solution():
    store_blocks = 11
    gallery_blocks = 6
    work_blocks = 8
    walked_blocks = 5

    # Calculate the total blocks Jess needs to walk
    total_blocks = store_blocks + gallery_blocks + work_blocks

    # Calculate the remaining blocks Jess needs to walk
    remaining_blocks = total_blocks - walked_blocks
    result = remaining_blocks
    return result

print(solution())