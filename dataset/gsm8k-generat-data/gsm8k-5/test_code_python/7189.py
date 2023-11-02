def solution():
    total_students = 11 + 13  # Total number of students in the class
    total_students_with_additional_boy = 12 + 13  # Total number of students in the class with 1 additional boy
    total_girls = 13  # Total number of girls in the class
    
    # Calculate the percentage of the class that are girls after the additional boy is added
    percent_girls = (total_girls / total_students_with_additional_boy) * 100
    result = percent_girls
    return result

print(solution())