def solution():
    total_students = 45
    speeders = (total_students - 3) / 7  # There are 3 less than 7 times as many speeders
    drunk_drivers = total_students - speeders  # The remaining students are drunk drivers
    result = drunk_drivers
    return result

print(solution())