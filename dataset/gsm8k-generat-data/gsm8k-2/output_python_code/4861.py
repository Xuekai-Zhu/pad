def solution():
    """In a 60-item exam, Liza got 90% of the items correctly. Her best friend, Rose, got 2 more correct answers than her. How many incorrect answers did Rose have?"""
    exam_items = 60
    liza_correct = int(exam_items * 0.9)
    rose_correct = liza_correct + 2
    rose_incorrect = exam_items - rose_correct
    result = rose_incorrect
    return result

print(solution())