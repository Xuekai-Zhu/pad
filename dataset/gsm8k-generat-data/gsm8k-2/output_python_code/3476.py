def solution():
    """Mr. Johnson is organizing the school Christmas play and needs 50 volunteers to help with decorating the auditorium. 5 students from each of the school’s 6 math classes have volunteered to help. 13 teachers have also volunteered to help. How many more volunteers will Mr. Johnson need?"""
    math_class_volunteers = 5 * 6
    total_volunteers = math_class_volunteers + 13
    more_volunteers_needed = 50 - total_volunteers
    result = more_volunteers_needed
    return result

print(solution())