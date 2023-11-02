def solution():
    students_per_class = 30  # Each class has 30 students
    # Calculate the number of students in Miss Johnson's class who prefer goldfish
    johnson_goldfish = 1/6 * students_per_class
    # Calculate the number of students in Mr. Feldstein's class who prefer goldfish
    feldstein_goldfish = 2/3 * students_per_class
    # Calculate the number of students in Ms. Henderson's class who prefer goldfish
    henderson_goldfish = 1/5 * students_per_class
    # Calculate the total number of students who prefer goldfish
    total_goldfish = johnson_goldfish + feldstein_goldfish + henderson_goldfish
    result = total_goldfish
    return result

print(solution())