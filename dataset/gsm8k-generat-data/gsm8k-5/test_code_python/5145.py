def solution():
    boys_percentage = 0.4  # Percentage of boys in the class
    girls_percentage = 1 - boys_percentage  # Percentage of girls in the class
    boys_grade = 0.8  # Average grade of boys on the math test
    girls_grade = 0.9  # Average grade of girls on the math test

    # Calculate the class average on the math test
    class_average = (boys_percentage * boys_grade) + (girls_percentage * girls_grade)
    result = class_average
    return result

print(solution())