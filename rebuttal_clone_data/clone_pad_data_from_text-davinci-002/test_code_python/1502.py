def solution():
    total_cupcakes = 2.5 * 12
    students_in_class = 27
    sick_students = 3
    total_people = students_in_class + 2
    cupcakes_given_away = total_people - sick_students
    remaining_cupcakes = total_cupcakes - cupcakes_given_away
    result = remaining_cupcakes
    return result

print(solution())