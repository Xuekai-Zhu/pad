def solution():
    total_items = 60
    Liza_correct = 90
    Liza_incorrect = total_items - Liza_correct
    Rose_correct = Liza_incorrect + 2
    Rose_incorrect = total_items - Rose_correct
    result = Rose_incorrect
    return result

print(solution())