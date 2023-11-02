def solution():
    num_gertrude_eggs = 4
    num_blanche_eggs = 3
    num_nancy_eggs = 2
    num_martha_eggs = 2
    num_dropped_eggs = 2

    # Calculate the total number of collected eggs
    total_collected_eggs = num_gertrude_eggs + num_blanche_eggs + num_nancy_eggs + num_martha_eggs

    # Calculate the number of remaining eggs after some were dropped
    num_remaining_eggs = total_collected_eggs - num_dropped_eggs
    result = num_remaining_eggs
    return result

print(solution())