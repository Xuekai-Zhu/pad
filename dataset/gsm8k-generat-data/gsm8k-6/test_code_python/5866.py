def solution():
    # Calculate the total number of people attending the ceremony
    num_graduates = 50
    num_parents = num_graduates * 2
    num_teachers = 20
    num_administrators = num_teachers / 2
    total_people = num_graduates + num_parents + num_teachers + num_administrators

    # Calculate the number of chairs needed for the ceremony
    num_chairs = total_people
    result = num_chairs
    return result

print(solution())