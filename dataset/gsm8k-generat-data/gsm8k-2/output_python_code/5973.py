def solution():
    """In a court-mandated traffic class, there are a certain number of drunk drivers and 3 less than 7 times that many speeders. If there are 45 students total, how many drunk drivers are there?"""
    total_students = 45
    speeders = (total_students - x)/7 + 3
    drunk_drivers = total_students - speeders
    result = drunk_drivers
    return result

print(solution())