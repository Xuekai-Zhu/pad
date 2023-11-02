def solution():
    people_on_trolley = 10
    people_off_trolley = 3
    people_on_trolley = people_on_trolley + (people_on_trolley - people_off_trolley)
    people_off_trolley = 18
    people_on_trolley = people_on_trolley - people_off_trolley
    people_on_trolley = people_on_trolley + 2
    result = people_on_trolley
    return result

print(solution())