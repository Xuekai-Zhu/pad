def solution():
    chairs_per_row = 6
    rows_of_chairs = 20
    people_per_chair = 5
    total_chairs = chairs_per_row * rows_of_chairs
    total_people = total_chairs * people_per_chair
    result = total_people
    return result

print(solution())