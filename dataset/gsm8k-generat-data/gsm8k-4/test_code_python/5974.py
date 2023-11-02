def solution():
    """In a court-mandated traffic class, there are a certain number of drunk drivers and 3 less than 7 times that many speeders. If there are 45 students total, how many drunk drivers are there?"""
    # Define the total number of students
    total_students = 45

    # Calculate the number of speeders
    speeders = (total_students - 3) / 7

    # Calculate the number of drunk drivers
    drunk_drivers = total_students - speeders

    # Return the result
    result = drunk_drivers
    return result

print(solution())