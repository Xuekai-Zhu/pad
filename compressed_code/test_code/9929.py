def solution():
    
    total_people = 20
    initial_girls_percent = 40
    initial_boys_percent = 100 - initial_girls_percent
    initial_girls = int((initial_girls_percent / 100) * total_people)
    initial_boys = total_people - initial_girls
    new_boys = 5
    new_total_people = total_people + new_boys
    new_girls = initial_girls
    new_boys_percent = (initial_boys + new_boys) / new_total_people * 100
    new_girls_percent = 100 - new_boys_percent
    result = new_girls_percent
    return result

print(solution())