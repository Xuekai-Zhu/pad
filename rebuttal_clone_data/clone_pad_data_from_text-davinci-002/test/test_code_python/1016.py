def solution():
    total_eggs = 1
    blue_eggs = 0.8
    purple_eggs = 0.2
    five_piece_eggs = 0.5 * purple_eggs + 0.25 * blue_eggs
    chance = five_piece_eggs * 100
    result = chance
    return result

print(solution())