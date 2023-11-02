def solution():
    total_items = 60  # The exam has 60 items
    liza_correct = int(total_items * 0.9)  # Liza got 90% of the items correctly
    rose_correct = liza_correct + 2  # Rose got 2 more correct answers than Liza
    total_correct = liza_correct + rose_correct  # Calculate the total correct answers
    incorrect = total_items - total_correct  # Calculate the total incorrect answers

    result = incorrect
    return result

print(solution())