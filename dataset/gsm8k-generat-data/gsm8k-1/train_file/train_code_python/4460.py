def solution():
    """Ms. Hatcher teaches 20 third-graders and a number of fourth-graders that is twice the number of third-graders. Her co-teacher asked her to substitute for her fifth-grade class that has half as many students as the number of third-graders. How many students did Ms. Hatcher teach for the day?"""
    third_graders = 20
    fourth_graders = third_graders * 2
    fifth_graders = third_graders / 2
    total_students = third_graders + fourth_graders + fifth_graders
    result = total_students
    return result

print(solution())