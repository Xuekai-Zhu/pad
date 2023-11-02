def solution():
    num_blouses_in_hamper = 0.75 * 12
    num_skirts_in_hamper = 0.5 * 6
    num_slacks_in_hamper = 0.25 * 8

    total_num_in_hamper = num_blouses_in_hamper + num_skirts_in_hamper + num_slacks_in_hamper

    num_to_wash = total_num_in_hamper
    result = num_to_wash
    return result

print(solution())