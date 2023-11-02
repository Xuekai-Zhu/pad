def solution():
    total_cans = 3 * 12
    total_people = 6
    people_with_3 = total_people / 2
    people_with_4 = 2
    people_with_5 = 1
    total_sodas = people_with_3 * 3 + people_with_4 * 4 + people_with_5 * 5
    sodas_leftover = total_cans - total_sodas
    result = sodas_leftover
    return result

print(solution())