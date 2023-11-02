def solution():
    
    total_students = 150
    percent_girls = 60
    percent_boys = 100 - percent_girls
    boys = (total_students * percent_boys) / 100
    varsity_boys = boys / 3
    non_varsity_boys = boys - varsity_boys
    result = non_varsity_boys
    
    return result

print(solution())