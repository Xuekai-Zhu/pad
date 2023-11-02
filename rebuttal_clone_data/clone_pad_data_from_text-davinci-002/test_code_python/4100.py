def solution():
    marathon_length = 26
    start_to_checkpoint1 = 1
    checkpoint4_to_finish = 1
    remaining_distance = marathon_length - start_to_checkpoint1 - checkpoint4_to_finish
    checkpoint_distance = remaining_distance / 3
    result = checkpoint_distance
    return result

print(solution())