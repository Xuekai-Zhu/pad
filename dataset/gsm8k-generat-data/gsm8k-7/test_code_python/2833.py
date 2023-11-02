def solution():
    num_students_per_class = 30

    # Calculate the number of students in Miss Johnson's class who prefer goldfish
    johnson_goldfish = num_students_per_class * (1/6)

    # Calculate the number of students in Mr. Feldstein's class who prefer goldfish
    feldstein_goldfish = num_students_per_class * (2/3)

    # Calculate the number of students in Ms. Henderson's class who prefer goldfish
    henderson_goldfish = num_students_per_class * (1/5)

    # Calculate the total number of students who prefer goldfish
    total_goldfish = johnson_goldfish + feldstein_goldfish + henderson_goldfish
    result = total_goldfish
    return result

print(solution())