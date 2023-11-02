def solution():
    total_walls = 9 * 4 + 4 * 5
    people = 5
    walls_per_person = total_walls // people
    result = walls_per_person
    return result

print(solution())