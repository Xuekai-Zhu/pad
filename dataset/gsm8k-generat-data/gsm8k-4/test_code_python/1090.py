def solution():
    """Beth had 150 students in her 10th-grade class. The following year 30 more students join. In her final year, 15 students left. How many students did Beth have in her class at the end of her final year?"""
    
    # Define the initial number of students
    initial_students = 150
    
    # Add the number of students who joined in the 11th grade
    students_11th_grade = initial_students + 30
    
    # Subtract the number of students who left in the final year
    students_final_year = students_11th_grade - 15
    
    result = students_final_year
    return result

print(solution())