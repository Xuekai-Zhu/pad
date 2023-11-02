def solution():
    """The number of students in Kylie's class is 50. In a particular test, ten students scored 90 marks, 15 scored ten marks fewer than the first ten students, and the rest scored 60 marks each. What are the average marks for the whole class?"""
    class_size = 50
    high_score = 90
    middle_score = 80  # 10 less than high score
    low_score = 60
    high_count = 10
    middle_count = 15
    low_count = class_size - high_count - middle_count

    total_score = (high_score * high_count) + (middle_score * middle_count) + (low_score * low_count)
    average_score = total_score / class_size
    result = average_score
    return result

print(solution())