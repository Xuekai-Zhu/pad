def solution():
    
    people = 10
    days = 10
    coal = 10000
    half_people = people / 2
    required_coal = 40000
    
    coal_per_person_per_day = coal / (people * days)
    
    days_needed = required_coal / (half_people * coal_per_person_per_day)
    result = days_needed
    return result

print(solution())