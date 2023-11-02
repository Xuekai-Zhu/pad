def solution():
    blocks_in_first_tower = 7
    blocks_in_second_tower = 7 + 5
    blocks_in_third_tower = 7 + 5 + 7
    blocks_in_first_tower_fell = 7
    blocks_in_second_tower_fell = 5 - 2
    blocks_in_third_tower_fell = 7 - 3
    total_blocks_fell = blocks_in_first_tower_fell + blocks_in_second_tower_fell + blocks_in_third_tower_fell
    result = total_blocks_fell
    return result

print(solution())