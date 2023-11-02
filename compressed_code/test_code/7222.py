def solution():
    
    swanson_average = 5
    jones_average = 6
    swanson_students = 25
    jones_students = 32
    swanson_zits = swanson_average * swanson_students
    jones_zits = jones_average * jones_students
    difference = jones_zits - swanson_zits
    result = difference
    return result

print(solution())