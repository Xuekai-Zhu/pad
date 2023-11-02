def solution():
    blocks_to_park = 4
    blocks_to_school = 7
    blocks_home = 11
    daily_walks = 3
    total_blocks = blocks_to_park + blocks_to_school + blocks_home
    result = total_blocks * daily_walks
    return result

print(solution())