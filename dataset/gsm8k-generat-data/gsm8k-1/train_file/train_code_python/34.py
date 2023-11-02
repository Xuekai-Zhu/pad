def solution():
    """Mr. Sanchez found out that 40% of his Grade 5 students got a final grade below B. How many of his students got a final grade of B and above if he has 60 students in Grade 5?"""
    total_students = 60
    percent_below_B = 40
    percent_above_B = 100 - percent_below_B
    students_above_B = total_students * (percent_above_B / 100)
    result = students_above_B
    return result

print(solution())