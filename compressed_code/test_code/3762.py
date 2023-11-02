def solution():
    
    exam_items = 60
    liza_correct = int(exam_items * 0.9)
    rose_correct = liza_correct + 2
    rose_incorrect = exam_items - rose_correct
    result = rose_incorrect
    return result

print(solution())