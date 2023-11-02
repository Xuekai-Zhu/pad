def solution():
    # Define Liza's score and total number of items
    liza_score = 0.9 * 60
    total_items = 60

    # Calculate Rose's score
    rose_score = liza_score + 2

    # Calculate Rose's number of incorrect answers
    rose_incorrect = total_items - rose_score

    result = rose_incorrect
    return result

print(solution())