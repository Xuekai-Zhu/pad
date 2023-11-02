def solution():
    girls = 60
    boy_ratio = 3/4
    girl_ratio = 4/4
    boys = girls * (boy_ratio / girl_ratio)

    teachers = 0.2 * boys

    total_people = girls + boys + teachers
    result = total_people
    return result

print(solution())