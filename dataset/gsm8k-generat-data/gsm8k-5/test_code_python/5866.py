def solution():
    # Calculate the total number of people attending the ceremony
    num_graduates = 50
    num_parents = num_graduates * 2
    num_teachers = 20
    num_administrators = num_teachers / 2
    total_attendees = num_graduates + num_parents + num_teachers + num_administrators

    # Calculate the number of chairs needed
    num_chairs = int(total_attendees)  # Round up to the nearest whole number

    result = num_chairs
    return result

print(solution())