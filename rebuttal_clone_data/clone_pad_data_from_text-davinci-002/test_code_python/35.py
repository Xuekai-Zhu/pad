def solution():
    """Mr. Sanchez found out that 40% of his Grade 5 students got a final grade below B. How many of his students got a final grade of B and above if he has 60 students in Grade 5?"""
    percent_below_b = 40
    total_students = 60
    students_above_b = total_students - (total_students * (percent_below_b / 100))
    result = students_above_b
    
    return result

print(solution())