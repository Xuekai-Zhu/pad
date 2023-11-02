def solution():
    """In a 60-item exam, Liza got 90% of the items correctly. Her best friend, Rose, got 2 more correct answers than her. How many incorrect answers did Rose have?"""
    # Define the total number of items in the exam
    total_items = 60

    # Calculate the number of correct answers Liza got
    liza_correct = total_items * 0.9

    # Calculate the number of correct answers Rose got
    rose_correct = liza_correct + 2

    # Calculate the number of incorrect answers Rose got
    rose_incorrect = total_items - rose_correct

    # return the result
    result = rose_incorrect
    return result

print(solution())