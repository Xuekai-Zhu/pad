def solution():
    
    boards_tested = 120
    tacks_remaining = 30
    tacks_per_board = 3
    total_tacks = (boards_tested * tacks_per_board) + (3 * tacks_remaining)
    result = total_tacks
    return result

print(solution())