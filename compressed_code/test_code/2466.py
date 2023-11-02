def solution():
    
    tape_per_small_box = 2 * 15 + 30
    tape_per_big_box = 2 * 40 + 40
    total_tape = 5 * tape_per_small_box + 2 * tape_per_big_box
    result = total_tape
    return result

print(solution())