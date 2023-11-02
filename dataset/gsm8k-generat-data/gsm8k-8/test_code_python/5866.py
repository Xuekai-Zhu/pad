def solution():
    # Calculate the number of parents attending
    num_parents = 2 * 50

    # Calculate the number of teachers attending
    num_teachers = 20

    # Calculate the number of administrators attending
    num_admins = num_teachers / 2

    # Calculate the total number of attendees
    total_attendees = num_parents + num_teachers + num_admins

    # Calculate the number of chairs needed
    num_chairs = total_attendees
    result = num_chairs
    return result

print(solution())