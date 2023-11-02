def solution():
    
    total_people = 600
    girls = 240
    boys = total_people - girls
    boys_left = boys * 0.25
    girls_left = girls * 0.125
    remaining_people = total_people - boys_left - girls_left
    result = remaining_people
    return result

print(solution())