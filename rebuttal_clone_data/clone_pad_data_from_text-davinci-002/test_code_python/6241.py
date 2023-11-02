def solution():
    oranges = 5
    pieces_per_orange = 8
    people = 4
    calories_per_orange = 80
    calories_per_person = (oranges * calories_per_orange) / people
    result = calories_per_person
    return result

print(solution())