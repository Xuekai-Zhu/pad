def solution():
    
    total_blouses = 12
    total_skirts = 6
    total_slacks = 8
    hamper_blouses = total_blouses * 0.75
    hamper_skirts = total_skirts * 0.5
    hamper_slacks = total_slacks * 0.25
    total_hamper = hamper_blouses + hamper_skirts + hamper_slacks
    result = total_hamper
    return result

print(solution())