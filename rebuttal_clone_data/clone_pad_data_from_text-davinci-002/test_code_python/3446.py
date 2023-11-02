def solution():
    total_people = 40
    people_on_bicycles = total_people * (3/5)
    people_on_tricycles = total_people - people_on_bicycles
    bicycles_in_race = people_on_bicycles
    tricycles_in_race = people_on_tricycles
    total_wheels = (bicycles_in_race * 2) + (tricycles_in_race * 3)
    result = total_wheels
    
    return result

print(solution())