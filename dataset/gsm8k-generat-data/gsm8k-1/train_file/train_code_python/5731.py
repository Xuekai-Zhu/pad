def solution():
    """The number of students in Kylie's class is 50. In a particular test, ten students scored 90 marks, 15 scored ten marks fewer than the first ten students, and the rest scored 60 marks each. What are the average marks for the whole class?"""
    num_students = 50
    high_score_num = 10
    high_score = 90
    lower_score_num = 15
    lower_score = high_score - 10
    other_score = 60
    total_score = (high_score * high_score_num) + (lower_score * lower_score_num) + (other_score * (num_students - high_score_num - lower_score_num))
    avg_score = total_score / num_students
    result = avg_score
    return result

print(solution())