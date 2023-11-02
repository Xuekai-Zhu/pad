def solution():
    """Ms. Mitsuko told the class that if the average score on their quiz is higher than 75% then they will get a pizza party. There are 25 students in the class. One student is absent and has to take the test the next day. The average score of the students who took the test was 77%. What is the lowest grade the absent student can get for the class to still get a pizza party?"""
    class_size = 25
    target_average = 0.75
    current_average = 0.77
    current_total = current_average * (class_size - 1)
    remaining_total = target_average * class_size
    lowest_possible_grade = (remaining_total - current_total) * 100
    result = lowest_possible_grade
    return result

print(solution())