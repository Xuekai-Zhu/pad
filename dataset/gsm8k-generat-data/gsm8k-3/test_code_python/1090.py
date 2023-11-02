def solution():
    """Beth had 150 students in her 10th-grade class.  The following year 30 more students join.  In her final year, 15 students left.  How many students did Beth have in her class at the end of her final year?"""
    # Define the initial number of students
    initial_students = 150
    
    # Add the number of students who joined in the 11th grade
    year_11_students = initial_students + 30
    
    # Subtract the number of students who left in the final year
    final_students = year_11_students - 15
    
    # Display the number of students in Beth's final year class
    result = final_students
    return result

print(solution())