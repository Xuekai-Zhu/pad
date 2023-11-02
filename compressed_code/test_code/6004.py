def solution():
    
    total_students = 18
    boys = 8
    girls = total_students - boys
    girls_on_trip = boys
    girls_not_on_trip = girls - girls_on_trip
    result = girls_not_on_trip
    return result

print(solution())