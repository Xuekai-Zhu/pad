def solution():
    """ Mr. Johnson is organizing the school Christmas play and needs 50 volunteers to help with decorating the auditorium. 5 students from each of the school’s 6 math classes have volunteered to help. 13 teachers have also volunteered to help. How many more volunteers will Mr. Johnson need?"""
    total_volunteers = (5 * 6) + 13
    volunteers_needed = 50
    additional_volunteers_needed = volunteers_needed - total_volunteers
    result = additional_volunteers_needed
    return result

print(solution())