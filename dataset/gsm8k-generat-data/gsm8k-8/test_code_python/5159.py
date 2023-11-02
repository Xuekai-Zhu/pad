def solution():
    # Count the total number of hands in the class
    total_hands = 20 + 2  # Including Peter's two hands
    
    # Divide by the number of hands per student
    students = total_hands / 2
    
    # Add one for Peter
    students += 1
    
    result = students
    return result

print(solution())