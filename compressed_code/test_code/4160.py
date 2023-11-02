def solution():
    
    girls = 60
    boys_ratio = 3/4
    boys = boys_ratio * girls
    teachers = 0.2 * boys
    total_people = girls + boys + teachers
    result = total_people
    return result

print(solution())