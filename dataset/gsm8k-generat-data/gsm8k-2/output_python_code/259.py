def solution():
    """Adam goes to a small school, which teaches 80 students in three classes. 40% of the students are in class A, and class B has 21 students fewer than class A. The rest are in class C. How many students are in this class?"""
    total_students = 80
    class_a_percent = 0.4
    class_a_students = total_students * class_a_percent
    class_b_students = class_a_students - 21
    class_c_students = total_students - class_a_students - class_b_students
    result = class_c_students
    return result

print(solution())