def solution():
    initial_people = 300
    initial_days = 90
    people_left = 100
    days_left = initial_days - 30
    people_remaining = initial_people - people_left
    days_per_person = days_left / people_remaining
    result = days_per_person
    return result

print(solution())