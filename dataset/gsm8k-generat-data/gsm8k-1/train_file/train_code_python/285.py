def solution():
    """There were 18 students assigned in a minibus for a field trip. Eight of these students were boys. On the day of the field trip, the number of girls and boys was the same since some of the girls were not able to join the trip. How many girls were not able to join the field trip?"""
    total_students = 18
    boys = 8
    girls = total_students - boys
    girls_on_trip = boys
    girls_not_on_trip = girls - girls_on_trip
    result = girls_not_on_trip
    return result

print(solution())