def solution():
    """Dani brings two and half dozen cupcakes for her 2nd-grade class. There are 27 students (including Dani), 1 teacher, and 1 teacher's aid. If 3 students called in sick that day, how many cupcakes are left after Dani gives one to everyone in the class?"""
    dozens_of_cupcakes = 2.5
    total_cupcakes = dozens_of_cupcakes * 12
    total_people = 27+1+1-3
    cupcakes_given = total_people
    cupcakes_left = total_cupcakes - cupcakes_given
    result = cupcakes_left
    return result

print(solution())