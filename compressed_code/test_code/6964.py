def solution():
    
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