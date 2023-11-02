def solution():
    
    total_students = 25
    girls_percent = 60
    boys_percent = 100 - girls_percent
    girls = total_students * (girls_percent / 100)
    boys = total_students - girls
    boys_basketball = boys * 0.4
    girls_basketball = 2 * (boys - boys_basketball)
    total_basketball = boys_basketball + girls_basketball
    percent_girls_basketball = (girls_basketball / girls) * 100
    result = percent_girls_basketball
    return result

print(solution())