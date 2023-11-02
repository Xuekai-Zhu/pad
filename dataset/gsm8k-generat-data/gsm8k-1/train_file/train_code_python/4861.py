def solution():
    """In a 60-item exam, Liza got 90% of the items correctly. Her best friend, Rose, got 2 more correct answers than her. How many incorrect answers did Rose have?"""
    total_items = 60
    liza_correct = 0.9 * total_items
    rose_correct = liza_correct + 2
    incorrect = total_items - (liza_correct + rose_correct)
    result = incorrect
    return result

print(solution())