def solution():
    ahmed_age = 11
    fouad_age = 26
    years = 0

    while (fouad_age != 2 * ahmed_age):
        fouad_age += 1
        ahmed_age += 1
        years += 1
    
    result = years
    return result

print(solution())