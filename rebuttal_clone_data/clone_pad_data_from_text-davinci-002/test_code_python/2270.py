def solution():
    total_students = 25
    girls = total_students * 0.6
    boys = total_students * 0.4
    boys_basketball = boys * 0.4
    girls_basketball = girls * 0.8
    total_basketball = boys_basketball + girls_basketball
    percent_girls_basketball = (girls_basketball / total_students) * 100
    result = percent_girls_basketball
    
    return result

print(solution())