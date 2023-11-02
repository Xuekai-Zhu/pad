def solution():
    
    van_capacity = 10
    minibus_capacity = 24
    num_vans = 6
    num_minibusses = 4
    total_students = (van_capacity * num_vans) + (minibus_capacity * num_minibusses)
    result = total_students
    return result

print(solution())