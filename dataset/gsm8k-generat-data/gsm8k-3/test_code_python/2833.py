def solution():
    """Annie does a survey of the sixth-grade classes to see who prefers pretzels to goldfish. In Miss Johnson's class, 1/6 of the students preferred goldfish. In Mr. Feldstein's class, 2/3rds of the students preferred goldfish. In Ms. Henderson's class, 1/5 of the students prefer goldfish. If each class has 30 students, how many people total prefer goldfish?"""
    # Define the number of students in each class and the fractions that prefer goldfish
    class_size = 30
    johnson_fraction = 1/6
    feldstein_fraction = 2/3
    henderson_fraction = 1/5

    # Calculate the number of students in each class that prefer goldfish
    johnson_goldfish = johnson_fraction * class_size
    feldstein_goldfish = feldstein_fraction * class_size
    henderson_goldfish = henderson_fraction * class_size

    # Calculate the total number of students that prefer goldfish
    total_goldfish = johnson_goldfish + feldstein_goldfish + henderson_goldfish

    # Display the total number of students that prefer goldfish
    result = total_goldfish
    return result

print(solution())