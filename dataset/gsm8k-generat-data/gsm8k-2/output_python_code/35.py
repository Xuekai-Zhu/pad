def solution():
    """Mr. Sanchez found out that 40% of his Grade 5 students got a final grade below B. How many of his students got a final grade of B and above if he has 60 students in Grade 5?"""
    total_students = 60
    below_b_students = total_students * 0.4
    above_b_students = total_students - below_b_students
    result = above_b_students
    return result

print(solution())