def solution():
    """Ms. Hatcher teaches 20 third-graders and a number of fourth-graders that is twice the number of third-graders. 
    Her co-teacher asked her to substitute for her fifth-grade class that has half as many students as the number of third-graders. 
    How many students did Ms. Hatcher teach for the day?"""
    
    # Calculate the number of fourth-graders
    fourth_graders = 2 * 20

    # Calculate the number of fifth-graders
    fifth_graders = 20 / 2

    # Calculate the total number of students that Ms. Hatcher taught for the day
    total_students = 20 + fourth_graders + fifth_graders
    
    # return the result
    result = total_students
    return result

print(solution())