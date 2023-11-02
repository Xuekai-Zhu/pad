def solution():
    total_blouses = 12
    total_skirts = 6
    total_slacks = 8
    blouses_in_hamper = total_blouses * 0.75
    skirts_in_hamper = total_skirts * 0.50
    slacks_in_hamper = total_slacks * 0.25
    total_clothes = blouses_in_hamper + skirts_in_hamper + slacks_in_hamper
    result = total_clothes
    return result

print(solution())