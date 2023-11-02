def solution():
    
    stories = 25
    apartments_per_floor = 4
    total_apartments = stories * apartments_per_floor
    people_per_apartment = 2
    total_people = total_apartments * people_per_apartment
    result = total_people
    return result

print(solution())