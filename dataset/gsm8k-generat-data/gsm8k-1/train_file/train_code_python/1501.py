def solution():
    """Dani brings two and half dozen cupcakes for her 2nd-grade class. There are 27 students (including Dani), 1 teacher, and 1 teacher's aid. If 3 students called in sick that day, how many cupcakes are left after Dani gives one to everyone in the class?"""
    cupcakes_per_dozen = 12
    cupcakes_per_student = 1
    total_students = 27
    total_staff = 2
    total_people = total_students + total_staff
    sick_students = 3
    cupcakes_brought = 2.5 * cupcakes_per_dozen
    cupcakes_given = total_people - sick_students
    cupcakes_left = cupcakes_brought - cupcakes_given
    result = cupcakes_left
    return result

print(solution())