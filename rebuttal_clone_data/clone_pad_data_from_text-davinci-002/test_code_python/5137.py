def solution():
    fifth_graders = 109
    sixth_graders = 115
    seventh_graders = 118
    chaperones_per_grade = 2 + 4
    students_per_bus = 72
    fifth_grade_ buses = math.ceil(fifth_graders / students_per_bus)
    sixth_grade_ buses = math.ceil(sixth_graders / students_per_bus)
    seventh_grade_ buses = math.ceil(seventh_graders / students_per_bus)
    buses_needed = fifth_grade_ buses + sixth_grade_ buses + seventh_grade_ buses
    result = buses_needed
    
    return result

print(solution())