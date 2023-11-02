def solution():
    total_people = 50
    percent_boys = 30
    boys = total_people * (percent_boys / 100)
    girls = total_people - boys
    result = girls
    
    return result

print(solution())