def solution():
    total_students = 45
    speeders = 7 * drunk_drivers - 3
    equation = drunk_drivers + speeders - total_students
    drunk_drivers = equation//8
    result = drunk_drivers
    return result

print(solution())