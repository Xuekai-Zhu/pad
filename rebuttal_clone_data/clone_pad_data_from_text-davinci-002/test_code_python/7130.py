def solution():
    people_starting = 19
    people_leaving = 2
    people_coming = 5
    people_remaining = people_starting + people_coming - people_leaving
    people_lifting = people_remaining - 5
    result = people_lifting
    return result

print(solution())