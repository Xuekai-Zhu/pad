def solution():
    """In a 60-item exam, Liza got 90% of the items correctly. Her best friend, Rose, got 2 more correct answers than her. How many incorrect answers did Rose have?"""
    # Define the total number of items in the exam
    total_items = 60

    # Calculate the number of items Liza got correctly
    liza_correct = int(total_items * 0.9)

    # Calculate the number of items Rose got correctly (2 more than Liza)
    rose_correct = liza_correct + 2

    # Calculate the number of incorrect answers Rose had
    rose_incorrect = total_items - rose_correct

    # Display the number of incorrect answers Rose had
    result = rose_incorrect
    return result

print(solution())