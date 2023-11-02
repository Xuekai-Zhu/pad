def solution():
    num_graduates = 50
    num_parents_per_graduate = 3  # graduate + 2 parents
    num_teachers = 20
    num_administrators = num_teachers / 2

    # Calculate the total number of people attending the ceremony
    total_people = (num_graduates * num_parents_per_graduate) + num_teachers + num_administrators

    # Calculate the number of chairs needed
    num_chairs = total_people
    result = num_chairs
    return result

print(solution())