def solution():
    """There are 92 students altogether. Twenty of them ride the school bus home together, 5/8 of the remaining ride their own bike home, and the rest whose houses are near the school walk home. How many students are walking home?"""
    total_students = 92
    bus_students = 20
    remaining_students = total_students - bus_students
    bike_students = (5/8) * remaining_students
    walking_students = remaining_students - bike_students
    result = walking_students
    
    return result

print(solution())