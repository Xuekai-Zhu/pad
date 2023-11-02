def solution():
    
    initial_people = 40
    initial_cans = 600
    percent_decrease = 30
    new_people = initial_people - (initial_people * (percent_decrease / 100))
    cans_per_person = initial_cans / initial_people
    new_cans = new_people * cans_per_person
    result = new_cans
    return result

print(solution())