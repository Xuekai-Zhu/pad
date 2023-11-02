def solution():
    beth_age = 18
    sister_age = 5
    years = 0

    while beth_age != 2 * sister_age:
        beth_age += 1
        sister_age += 1
        years += 1

    result = years
    return result

print(solution())