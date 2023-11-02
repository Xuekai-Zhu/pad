def solution():
    
    total_people = 300
    attendees = total_people / 2
    males = attendees * (2/3)
    females = attendees - males
    result = females
    return result

print(solution())