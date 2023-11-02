def solution():
    num_items = 60
    liza_correct = 0.9 * num_items
    rose_correct = liza_correct + 2

    # Calculate the number of incorrect answers for Liza
    liza_incorrect = num_items - liza_correct

    # Calculate the number of incorrect answers for Rose
    rose_incorrect = num_items - rose_correct

    result = rose_incorrect
    return result

print(solution())