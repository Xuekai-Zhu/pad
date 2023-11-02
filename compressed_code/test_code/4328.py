def solution():
    
    rick_age = 15
    oldest_brother_age = 2 * rick_age
    middle_brother_age = oldest_brother_age / 3
    smallest_brother_age = middle_brother_age / 2
    youngest_brother_age = smallest_brother_age - 2
    result = youngest_brother_age
    return result

print(solution())