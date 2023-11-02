def solution():
    
    total_people = 133
    boy_girl_difference = 33
    total_boys = (total_people + boy_girl_difference) / 2
    total_girls = total_people - total_boys
    result = total_girls
    return result

print(solution())