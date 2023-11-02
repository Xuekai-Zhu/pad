def solution():
    total_people = 600
    boys_leaving = total_people / 4
    girls_leaving = total_people / 8
    people_remaining = total_people - boys_leaving - girls_leaving
    result = people_remaining
    return result

print(solution())